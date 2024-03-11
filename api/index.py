import os
from fastapi import FastAPI

app = FastAPI()

CLIENT_TOKEN = os.getenv("WEBHOOK_TOKEN")

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/webhook")
def webhook(
    clientToken: str,
    secret: str
):
    if clientToken != CLIENT_TOKEN:
        raise ValueError("Invalid client token")
    return secret
