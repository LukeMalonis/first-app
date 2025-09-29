# Railway deploy test
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mesage": "Hello World"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}