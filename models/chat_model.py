import httpx
import os
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
from dotenv import load_dotenv
load_dotenv()
from starlette.responses import StreamingResponse
import json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # recommended for security

async def run(prompt: str, max_retries: int = 3):
    if not prompt:
        return {"error": "No prompt provided"}
    #logging.info(f"The value of my_variable is: {OPENAI_API_KEY}")
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",  # or "gpt-4"
        "messages": [
            {"role": "system", "content": "You are a helpful yoga assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    retries = 0
    while retries <= max_retries:
        try:
            async with httpx.AsyncClient(timeout=20.0) as client:
                response = await client.post(url, headers=headers, json=payload)
                if response.status_code == 429:
                    await asyncio.sleep(2 ** retries)  # exponential backoff
                    retries += 1
                    continue
                response.raise_for_status()
                data = response.json()
                return {
                    "response": data["choices"][0]["message"]["content"]
                }
        except httpx.HTTPError as e:
            return {"error": str(e)}

    return {"error": "Exceeded retry limit due to rate limiting"}

async def stream(prompt: str):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful yoga assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": True,
        "temperature": 0.7,
        "max_tokens": 200
    }

    async def event_stream():
        async with httpx.AsyncClient(timeout=60.0) as client:
            async with client.stream("POST", url, headers=headers, json=payload) as response:
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        payload = line[len("data: "):]
                        if payload.strip() == "[DONE]":
                            break
                        try:
                            chunk = json.loads(payload)
                            token = chunk["choices"][0]["delta"].get("content", "")
                            yield token
                        except Exception:
                            continue

    return StreamingResponse(event_stream(), media_type="text/plain")
