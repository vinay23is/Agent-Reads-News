import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_latest_news():
    query = "latest trending global news"
    api_key = os.getenv("NEWS_API_KEY")
    url = (
        "https://newsapi.org/v2/top-headlines?language=en&category=general&apiKey=a8a6581750c24f12af661281664aa49a"
    )
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = response.json().get("articles", [])
    print(data)
    if not articles:
        return "No trending news found."
    return articles[0]["title"] + ". " + articles[0]["description"]
    # article = data["articles"][0]
    # return f"{article['title']}\n\n{article['description']}"
