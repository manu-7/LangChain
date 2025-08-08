from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/essay/invoke")
async def generate_essay(request: Request):
    data = await request.json()
    topic = data.get("input", {}).get("topic", "Global Warming")

    # Prompt to send to the AI
    prompt = f"Write a detailed essay about {topic} in 500 words."

    # Call phi model via Ollama
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi",
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        result = response.json()
        return {"output": {"content": result.get("response", "Failed to generate essay.")}}
    else:
        return {"output": {"content": "Failed to connect to AI."}}
