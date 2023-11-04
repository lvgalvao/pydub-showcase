from pathlib import Path

from pydub import AudioSegment

# Define the base assets directory
assets_dir = Path("assets/inputs")
assets_out = Path("assets/inputs")

# Define the source file paths
bass_wav_path = assets_dir / "bass.wav"
pads_wav_path = assets_dir / "pads.wav"
drums_wav_path = assets_dir / "drums.wav"

# Load the audio file
bass = AudioSegment.from_file(bass_wav_path)
pads = AudioSegment.from_file(pads_wav_path)
drums = AudioSegment.from_file(drums_wav_path)

# Concatene the audio files using append and cross fade

bass_pads_with_crossfade = bass[5_000:9_000].append(pads[5_000:10_000], crossfade=4_000)

bass_pads_with_crossfade.export(
    assets_out / "bass_pads_with_crossfade.mp3", format="mp3"
)

# Concatene the audio files using overlay

bass_pads_drums_using_over_load = pads.overlay(bass).overlay(drums)[5_000:10_000]

bass_pads_drums_using_over_load.export(
    assets_out / "bass_pads_drums_using_over_load.mp3", format="mp3"
)
