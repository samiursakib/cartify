import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Cartify!"}

def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)
