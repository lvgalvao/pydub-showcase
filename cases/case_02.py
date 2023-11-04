from pathlib import Path

from pydub import AudioSegment

# Define the base assets directory
assets_dir = Path("assets")

# Define the source file paths
bass_wav_path = assets_dir / "bass.wav"

# Load the audio file
bass = AudioSegment.from_file(bass_wav_path)

# Metadata about the audio file

print(f"Channels: {bass.channels}")
print(f"Sample width: {bass.sample_width}")
print(f"Frame rate: {bass.frame_rate}")
print(f"Duration: {bass.duration_seconds}")
print(f"Maximum amplitude: {bass.max}")
print(f"Average amplitude: {bass.rms}")
