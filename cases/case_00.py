from pathlib import Path

from pydub import AudioSegment
from pydub.playback import play

# Define the base assets directory
assets_dir = Path("assets")

# Define the source and target file paths
bass_wav_path = assets_dir / "bass.wav"
bass_mp3_path = assets_dir / "bass.mp3"

# Load the audio file
bass = AudioSegment.from_file(bass_wav_path)

# Export the audio file to a different format
bass.export(bass_mp3_path, format="mp3")

# Play the audio file
play(bass)
