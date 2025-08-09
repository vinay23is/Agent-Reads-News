Perfect — let’s turn this into the **fine-grained “chef’s secret cookbook”** for *Agent Reads News*.
This will include **everything**:

* Step-by-step recipe flow
* Every ingredient (library, API, function) with *why it’s there*
* Example API calls & JSON responses
* Code walkthroughs line-by-line where useful
* Design trade-offs
* Interview talking points you can drop in naturally

---

# 📰 AGENT READS NEWS – THE CHEF’S SECRET COOKBOOK

Welcome to your **kitchen for news automation**.
We’re going to **source fresh stories**, **cook them down into digestible bites**, and, if you want, **plate them up with a side of audio**.
By the end of this, you’ll be able to explain this project in an interview like it’s your signature dish.

---

## 🛒 INGREDIENTS (AND WHY WE’RE USING THEM)

| Ingredient          | Role in Recipe      | Why This Choice                                                        |
| ------------------- | ------------------- | ---------------------------------------------------------------------- |
| **Python 3.8+**     | Main kitchen        | Mature, lots of support for HTTP requests, AI APIs, and audio handling |
| **requests**        | The waiter          | Simple, reliable HTTP requests for fetching news & sending to APIs     |
| **python-dotenv**   | Secret spice drawer | Loads `.env` API keys so they’re never hardcoded                       |
| **NewsAPI.org**     | The farmer’s market | Free tier, clean JSON, lets you filter by topic/date                   |
| **Gemini / OpenAI** | Master chef         | Turns raw articles into a polished script                              |
| **ElevenLabs**      | The DJ              | Reads your news out loud with a human voice                            |
| **json**            | Ingredient sorter   | Easy parsing of API responses                                          |
| **os**              | Kitchen organizer   | Grabs API keys from environment variables                              |
| **io / tempfile**   | Takeaway containers | Handles audio files in memory before saving                            |

---

## 📋 THE MENU (PROJECT LAYOUT)

```
agent-reads-news/
│── main.py                     # The head chef – runs everything
│── requirements.txt            # Shopping list of ingredients
│── start_tts_env.bat            # Windows-only TTS setup helper
│── test.txt                     # Sample dish to test TTS
└── utils/
    ├── fetch_news.py            # Fetches raw headlines
    ├── news_search_tool.py      # Filters and searches fetched news
    ├── structure_with_gemini.py # Summarizes with AI
    ├── text_to_speech.py        # Turns text into audio
    └── tts_tool.py              # Extra tools for audio processing
```

---

## 📜 FULL RECIPE (WORKFLOW)

### **Step 1: Fetch Fresh News** – `fetch_news.py`

**Code Essence:**

```python
import os, requests

def fetch_latest_news(topic="technology", max_results=5):
    api_key = os.getenv("NEWS_API_KEY")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "pageSize": max_results,
        "sortBy": "publishedAt",
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("articles", [])
```

**Sample API Call:**

```
GET https://newsapi.org/v2/everything?q=technology&pageSize=5&sortBy=publishedAt&apiKey=YOUR_KEY
```

**Sample JSON Response (trimmed):**

```json
{
  "status": "ok",
  "articles": [
    {
      "source": {"id": null, "name": "TechCrunch"},
      "author": "Jane Doe",
      "title": "OpenAI launches GPT-5",
      "description": "The latest model offers better reasoning...",
      "url": "https://techcrunch.com/article",
      "publishedAt": "2025-08-09T10:00:00Z"
    }
  ]
}
```

---

### **Step 2: Summarize & Structure** – `structure_with_gemini.py`

**Prompt Design (the recipe for AI):**

```
Summarize the following articles into a short, engaging news script:
1. TITLE – DESCRIPTION
2. TITLE – DESCRIPTION
...
Make it clear, concise, and listener-friendly.
```

**Gemini API Call (example with pseudo-code):**

```python
import os, requests

def summarize_news(articles):
    api_key = os.getenv("GEMINI_API_KEY")
    content = "\n".join([f"{i+1}. {a['title']} - {a['description']}" for i,a in enumerate(articles)])
    prompt = f"Summarize the following into a short script:\n{content}"
    # Example POST to Gemini endpoint here (pseudo-code)
    response = requests.post("https://gemini.googleapis.com/v1/summarize", headers=..., json=...)
    return response.json()["summary"]
```

**OpenAI Alternate (if Gemini not set):**

```python
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role":"system","content":"You are a news summarizer"},
              {"role":"user","content": prompt}]
)
```

---

### **Step 3: Convert to Speech (Optional)** – `text_to_speech.py`

**ElevenLabs API Call:**

```python
import os, requests

def convert_to_speech(text, output_file="news.mp3"):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {"text": text, "voice_settings": {"stability": 0.75, "similarity_boost": 0.85}}
    response = requests.post(url, json=payload, headers=headers)
    with open(output_file, "wb") as f:
        f.write(response.content)
```

**Output:**
`news.mp3` — a clean, realistic voice reading your AI-generated script.

---

## 🎨 DESIGN TRADE-OFFS & WHY

* **Separate Modules** → Easier testing & swapping APIs.
* **Prompt Structure** → Bullet-style input helps AI stay concise.
* **Optional TTS** → Keeps project usable for text-only workflows.
* **No Database** → Simple scripts keep it fast & portable; you can add DB later for storage.

---

## 💬 INTERVIEW ONE-LINERS

* “We separated fetching, summarization, and TTS into modules so changing providers is a drop-in replacement.”
* “The LLM prompt is designed for clarity and brevity, optimized for spoken delivery.”
* “By keeping API keys in `.env`, we ensure no secrets leak in source control.”
* “Scaling could be done by batching API calls and caching summaries.”


