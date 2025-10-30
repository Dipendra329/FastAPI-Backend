import fastapi
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
def hello_world():
    return "hello world"


@app.get("/")
def home():
    return "welcome to home!" 


@app.get("/status")
def status():
    return "everything is working!"

