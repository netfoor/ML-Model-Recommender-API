# token_estimator.py
def estimate_tokens(text: str) -> int:
    """Estimate tokens using word/token ratio with buffer"""
    word_count = len(text.split())
    return int(word_count * 1.5)  # 1 token ≈ 1.33 words + 20% buffer