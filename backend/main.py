import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("backend/.env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=request.message
    )

    return {"reply": response.output_text}