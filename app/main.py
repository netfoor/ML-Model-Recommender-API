from fastapi import FastAPI, Request
from mangum import Mangum
from .recommender import recommend_best_model

app = FastAPI()

@app.post("/recommend-model")
async def recommend_model(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    provider = body.get("provider")

    result = recommend_best_model(prompt, provider)
    return result
    
handler = Mangum(app)
