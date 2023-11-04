from pathlib import Path

from pydub import AudioSegment
from pydub.playback import play

# Define the base assets directory
assets_dir = Path("assets")

# Define the source file paths
bass_wav_path = assets_dir / "bass.wav"
pads_wav_path = assets_dir / "pads.wav"

# Load the audio file
bass = AudioSegment.from_file(bass_wav_path)
pads = AudioSegment.from_file(pads_wav_path)

# Remove the first 5 seconds and the last 5 seconds from bass

new_bass = bass[1_000 * 5 : -1_000 * 20]

new_pads = pads[1_000 * 5 : -1_000 * 20]

# Combine the audio files
combined = new_bass + new_pads

# Play the audio file
play(combined)
