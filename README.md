# AGENT READS NEWS

Agent Reads News is a Python-based application that **automatically fetches the latest news, summarizes it using a Large Language Model (LLM), and can optionally convert the summaries into speech**.
It is built to be **modular**, so you can easily swap out news sources, LLM providers, or TTS engines without changing the whole codebase.

This project is ideal for:

* Quickly staying updated on news without reading full articles.
* Building automated news podcast-like audio.
* Experimenting with LLM-based content structuring and Text-to-Speech integration.

---

## FEATURES

* **NEWS FETCHING:** Pulls fresh articles from APIs such as NewsAPI.org.
* **SUMMARIZATION:** Uses Gemini or OpenAI to rewrite and structure the news into short, clear scripts.
* **TEXT-TO-SPEECH:** Converts summaries into spoken audio using ElevenLabs (optional).
* **MODULAR DESIGN:** Utilities are separated into `utils/` so you can customize or replace parts without breaking the workflow.
* **CROSS-PLATFORM:** Works on Windows, macOS, and Linux.

---

## PROJECT STRUCTURE

```
agent-reads-news/
│── main.py                     # Entry point for running the app
│── requirements.txt            # Python dependencies
│── start_tts_env.bat            # Windows batch file to start TTS environment
│── test.txt                     # Sample text file for testing
└── utils/
    ├── fetch_news.py            # Functions for fetching articles
    ├── news_search_tool.py      # Search/filter news utility
    ├── structure_with_gemini.py # Summarization logic using Gemini/OpenAI
    ├── text_to_speech.py        # Converts text to speech
    └── tts_tool.py              # Helper functions for TTS
```

---

## REQUIREMENTS

* Python 3.8+
* An API key for at least one LLM provider (Gemini or OpenAI)
* An API key for a news provider (e.g., NewsAPI.org)
* (Optional) An API key for ElevenLabs if using Text-to-Speech.

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ENVIRONMENT VARIABLES

The application reads API keys from environment variables.
You can create a `.env` file or set them in your shell before running.

Example `.env`:

```
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
NEWS_API_KEY=your_newsapi_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here
```

> Only include variables for the services you are actually using. Keep keys private.

---

## USAGE

Run from the command line:

```bash
python main.py
```

If using Streamlit (check if your version supports it):

```bash
streamlit run main.py
```

---

## HOW IT WORKS

1. **Fetching News**

   * `fetch_news.py` calls the news API and retrieves recent articles.
   * Optionally, `news_search_tool.py` can filter results by keywords or topics.

2. **Summarizing & Structuring**

   * `structure_with_gemini.py` sends fetched articles to an LLM (Gemini or OpenAI).
   * The LLM condenses articles into short, clear, well-structured summaries.

3. **Converting to Audio (Optional)**

   * `text_to_speech.py` and `tts_tool.py` take the summaries and convert them into spoken audio files using ElevenLabs.

---

## TIPS

* Be aware of API rate limits for your providers.
* Test your `.env` setup before running the application.
* Pin library versions in `requirements.txt` for consistent behavior across machines.
* If adapting this repo from someone else’s project, keep original licensing intact.

---

## FUTURE IMPROVEMENTS

* Add support for more news APIs.
* Allow multiple voices and languages for TTS.
* Automate publishing as a daily news podcast.

---

## LICENSE

MIT License (or the license you choose to apply).
Make sure to add a `LICENSE` file if missing.


