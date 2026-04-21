from .db import get_all_models
from .classifier import classify_prompt
from .token_estimator import estimate_tokens

def recommend_best_model(
    prompt: str,
    provider: str = None,
    expected_output_length: int = 200,  # Default expected token count for completion
    quality_priority: bool = False,
    budget: float = None
) -> dict:
    """
    Recommends optimal model based on:
    - Prompt complexity
    - Token requirements
    - Model capabilities
    - Cost efficiency
    - Quality vs cost tradeoffs
    """
    # 1. Analyze prompt characteristics
    complexity = classify_prompt(prompt)
    prompt_tokens = estimate_tokens(prompt)
    total_tokens_required = prompt_tokens + expected_output_length
    
    # 2. Retrieve available models
    models = get_all_models(provider)
    if not models:
        return {"error": "No models available for selected provider"}
    
    # 3. Filter viable candidates
    viable_models = []
    for model in models:
        # Check context window size
        if model["context_length"] < total_tokens_required:
            continue
        
        # Check quality requirements
        quality_ok = (
            (complexity == "complex" and model["quality_score"] >= 8) or
            (complexity == "medium" and model["quality_score"] >= 6) or
            (complexity == "simple" and model["quality_score"] >= 4)
        )
        if not quality_ok:
            continue
            
        # Estimate costs
        prompt_cost = prompt_tokens * model["price_prompt"]
        completion_cost = expected_output_length * model["price_completion"]
        total_cost = prompt_cost + completion_cost
        
        # Budget check
        if budget and total_cost > budget:
            continue
            
        viable_models.append({
            **model,
            "total_cost": total_cost,
            "cost_breakdown": {
                "prompt": prompt_cost,
                "completion": completion_cost
            }
        })
    
    if not viable_models:
        return {"error": "No models meet requirements"}
    
    # 4. Select best model based on priority
    if quality_priority:
        viable_models.sort(key=lambda x: (-x["quality_score"], x["total_cost"]))
    else:
        viable_models.sort(key=lambda x: (x["total_cost"], -x["quality_score"]))
    
    best_model = viable_models[0]
    
    # 5. Generate explanation
    explanation = {
        "complexity": complexity,
        "prompt_tokens": prompt_tokens,
        "total_tokens_estimated": total_tokens_required,
        "selection_reason": "Quality priority" if quality_priority else "Cost efficiency"
    }
    
    return {
        "provider": best_model["provider"],
        "model": best_model["model"],
        "total_cost": best_model["total_cost"],
        "cost_breakdown": best_model["cost_breakdown"],
        "quality_score": best_model["quality_score"],
        "context_window": best_model["context_length"],
        "explanation": explanation
    }