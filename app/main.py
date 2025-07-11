from fastapi import FastAPI
from mangum import Mangum
from .recommender import recommend_model
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()

@app.post("/recommend-model")
async def recommend(request: Request):
    data = await request.json()
    task = data.get("task")
    if not task:
        return JSONResponse(content={"error": "Task is required"}, status_code=400)
    result = recommend_model(task)
    return JSONResponse(content=result)

handler = Mangum(app)
