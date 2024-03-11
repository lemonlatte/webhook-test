import os
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

CLIENT_TOKEN = os.getenv("WEBHOOK_TOKEN")

class WebhookPayload(BaseModel):
    clientToken: str
    secret: str

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/webhook")
def webhook(payload: WebhookPayload):
    if payload.clientToken != CLIENT_TOKEN:
        raise ValueError("Invalid client token")
    return payload.secret
