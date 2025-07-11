from app.recommender import recommend_model

def test_summarization_task():
    result = recommend_model("summarization")
    assert "model" in result
    assert result["provider"] == "openai"

def test_invalit_task():
    result = recommend_model("non_existent_task")
    assert "error" in result
    assert result["error"] == "No models found for task: non_existent_task"