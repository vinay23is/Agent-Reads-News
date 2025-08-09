# utils/text_to_speech.py
from TTS.api import TTS
import torch
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs  # Import the required globals
from TTS.config.shared_configs import BaseDatasetConfig  # Import the additional required global

# Allowlist the necessary globals for safe loading
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize TTS model (voice cloning + multilingual)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
#tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)

def speak(text, speaker_wav_path, output_path="C:/Users/DELL/Downloads/output_audio.wav"):
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav_path,
        language="en",  # Adjust to "en-IN" if supported in your prompt or speaker style
        file_path=output_path
    )
    print(f"✅ Audio saved to {output_path}")