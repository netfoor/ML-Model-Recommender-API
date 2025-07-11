from .config import load_models_config


def recommend_model(task: str) -> dict:
    models = load_models_config()
    # Filter models that support this task
    candidates = [m for m in models if task in m["tasks"]]
    if not candidates:
        return {"error": f"No models found for task: {task}"}
    # Sort by total cost
    sorted_models = sorted(
        candidates, 
        key=lambda m: m["cost_input"] + m["cost_output"]
    )
    best = sorted_models[0]
    return {
        "provider": best["provider"],
        "model": best["name"],
        "reason": f"Best trade-off cost/speed for task: {task}",
        "approx_cost_per_1k_tokens": best["cost_input"] + best["cost_output"],
        "max_context_length": best["context_length"],
        "speed": best["speed"]
    }
