# from google.adk import Agent
# from agent_tools.fetch_news import NewsSearchTool
# from agent_tools.tts_tool import TextToSpeechTool
# from google.adk.agents import LlmAgent
# from google.adk.runtime import run_agent


# agent = Agent(
#     name="NewsReaderAgent",
#     tools=[NewsSearchTool],
#     # workflow=[
#     #     "NewsSearchTool"
#     # ]
#     instruction="You are a newsreader agent. Fetch trending news and present it clearly."
# )



# runtime = AgentRuntime()
# response = runtime.run(agent, "Give me the latest global news")
# print(response.response)

from utils.fetch_news import fetch_latest_news
from utils.structure_with_gemini import structure_news
from utils.text_to_speech import speak

def main():
    print("🔍 Fetching news...")
    raw_news = fetch_latest_news()
    
    print("\n🧠 Structuring news with Gemini...")
    formatted_news = structure_news(raw_news)
    print(f"\n🎙️ Structured News:\n{formatted_news}")

    print("\n🗣️ Converting to speech...")
    speak(formatted_news, speaker_wav_path="C:/Users/DELL/Downloads/p_48189067_926.mp3")

if __name__ == "__main__":
    main()
