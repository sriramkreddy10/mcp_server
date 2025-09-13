import httpx
import os
import asyncio

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<your_openai_key_here>")

async def run(user_input: str):
    if not user_input:
        return {"error": "No input provided"}

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an AI router in a model-compute orchestration system.

Based on the user's input, decide which task type to perform from this list:
["summarize", "translate", "chat", "recommend", "analyze"]

Respond ONLY with a JSON object like:
{{ "action": "summarize" }}

User input: "{user_input}"
"""

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 50
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            response_text = result["choices"][0]["message"]["content"]
            # Very basic JSON parse
            if '"action":' in response_text:
                import json
                try:
                    parsed = json.loads(response_text.strip())
                    return {"action": parsed["action"]}
                except:
                    return {"error": "Invalid JSON returned from LLM"}
            else:
                return {"error": "No action detected in response"}
    except httpx.HTTPError as e:
        return {"error": f"Router model error: {str(e)}"}
