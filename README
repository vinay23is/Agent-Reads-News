Agent-Reads-News
A lightweight Python agent that fetches recent news, structures a short script with an LLM, and (optionally) turns it into audio for quick listening.

Built from a simple CLI (main.py) and modular helpers in utils/ for news fetching, text structuring (Gemini/OpenAI), and TTS.

Features
🔎 Fetches fresh news from configured sources

✍️ Summarizes & structures stories with an LLM

🔊 Optional text-to-speech output

🧩 Modular utils so you can swap providers easily

Project Structure
css
Copy
Edit
Agent-Reads-News/
  ├─ main.py
  ├─ requirements.txt
  ├─ start_tts_env.bat
  ├─ test.txt
  └─ utils/
      ├─ fetch_news.py
      ├─ news_search_tool.py
      ├─ structure_with_gemini.py
      ├─ text_to_speech.py
      └─ tts_tool.py
Tech & APIs
Language: Python

Core libs: see requirements.txt

Possible external APIs (depending on your setup):

Google Gemini API (for structuring/summaries)

OpenAI API (alternative LLM flow)

NewsAPI.org (news retrieval)

ElevenLabs (TTS)

Setup
bash
Copy
Edit
# 1) (Recommended) create a virtual env
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt
Environment Variables
Create a .env file or export in your shell. Include only what you use.

bash
Copy
Edit
# LLMs (pick one or both)
export GEMINI_API_KEY=...
export OPENAI_API_KEY=...

# News provider
export NEWS_API_KEY=...          # e.g., NewsAPI.org

# TTS (optional)
export ELEVENLABS_API_KEY=...
Keep keys private. Consider a secrets manager for production.

Run
Basic run (CLI):

bash
Copy
Edit
python main.py
If using Streamlit:

bash
Copy
Edit
streamlit run main.py
Check main.py for any flags or configurable constants (topics, date ranges, output paths).

How It Works
Fetch – utils/fetch_news.py & utils/news_search_tool.py retrieve recent articles.

Structure – utils/structure_with_gemini.py (or OpenAI) condenses items into a concise script.

Voice (optional) – utils/text_to_speech.py & utils/tts_tool.py convert text to audio.

Tips
Watch API rate limits.

Pin versions in requirements.txt for reproducibility.

If forked from another repo, keep license and attribution.

License
MIT (or your choice). Add a LICENSE file if missing.

