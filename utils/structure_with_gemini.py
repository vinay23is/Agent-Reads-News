import requests
import os
from dotenv import load_dotenv

load_dotenv()

def structure_news(news_text):
    api_key = os.getenv("GEMINI_API_KEY")
    prompt = (
        "Format the following news article into a short, broadcast-ready news script:\n\n"
        f"{news_text}"
    )
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
        params={"key": api_key},
        json={"contents": [{"parts": [{"text": prompt}]}]},
    )
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
