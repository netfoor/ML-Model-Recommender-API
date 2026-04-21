def classify_prompt(prompt: str) -> str:
    """
    Classify a prompt as simple, medium, or complex using multiple features:
    1. Complex keywords
    2. Role phrases
    3. Step indicators
    4. Verb complexity
    5. Word count
    """
    prompt_lower = prompt.lower()
    words = prompt_lower.split()
    word_count = len(words)

    # 1. Complex keywords (immediate complex classification)
    complex_keywords = {"autonomous", "strategy", "plan", "integrate", "self-heal", "mcp", 
                        "orchestrate", "dynamic", "framework", "synthesize"}
    if any(kw in prompt_lower for kw in complex_keywords):
        return "complex"

    points = 0
    
    # 2. Role phrases
    role_phrases = {
        "you are", "act as", "role:", "as a", "you will be", 
        "i want you to be", "you're", "acting as"
    }
    if any(role in prompt_lower for role in role_phrases):
        points += 1

    # 3. Step indicators
    step_indicators = {
        "first", "then", "next", "after", "finally", "step", 
        "steps", "start", "begin", "end", "lastly", "subsequently"
    }
    if any(step in words for step in step_indicators):
        points += 1

    # 4. Complex verbs
    complex_verbs = {
        # Base forms
        "write", "create", "generate", "plan", "analyze", "integrate", "manage", 
        "develop", "design", "build", "compose", "formulate", "implement", 
        "engineer", "optimize", "suggest", "recommend", "evaluate", "adapt",
        # Common conjugations
        "writes", "writing", "wrote", "created", "creating", "creates",
        "generates", "generating", "generated", "planned", "planning", 
        "analyzed", "analyzing", "integrates", "integrating", "integrated",
        "manages", "managing", "developed", "developing", "designed", 
        "designing", "built", "building", "composed", "composing", 
        "formulated", "formulating", "implemented", "implementing", 
        "engineered", "engineering"
    }
    if any(verb in words for verb in complex_verbs):
        points += 1

    # 5. Word count scoring
    if word_count > 30:
        points += 2
    elif word_count > 10:
        points += 1

    # Classification
    if points == 0:
        return "simple"
    elif points == 1:
        return "medium"
    else:
        return "complex"
