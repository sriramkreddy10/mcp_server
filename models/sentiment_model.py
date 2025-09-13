async def run(text: str):
    if not text:
        return {"error": "No input text provided"}
    
    text = text.lower()
    
    if "bad" in text or "hate" in text:
        return {"sentiment": "negative"}
    elif "good" in text or "love" in text or "amazing" in text:
        return {"sentiment": "positive"}
    else:
        return {"sentiment": "neutral"}
