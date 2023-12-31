# Just a Pydub showcase

Pydub is a simple and easy-to-use library for audio manipulation. It is written in pure Python and does not require any external libraries. It can read, filter, and modify audio files.

Imagine a project that requires a conversation with any LLM model. So, you need to read an audio file, fill the gaps, and silence it before sending it to the model. Pydub makes this process easy.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

You can install it with the following command:

```bash
poetry install
```

## Cases

- cases/case_00.py - Read an audio file and save it in another format.
- cases/case_01.py - Slice two audio files and concatenate them.
- cases/case_02.py - Show the audio file's metadata.
- cases/case_03.py - [Crossfade](assets/bass_pads_with_crossfade.mp3) and [Overlay](assets/bass_pads_drums_using_over_load.mp3) two audio files.
