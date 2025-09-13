def run(text: str):
    if not text or len(text.strip()) == 0:
        return {"error": "No input text provided"}
    
    # Naive summarization: return first sentence (mock logic)
    summary = text.split('.')[0] + '.' if '.' in text else text
    return {"summary": summary.strip()}
