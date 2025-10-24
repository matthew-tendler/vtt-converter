# VTT Converter

This tool converts Zoom .vtt transcript files into clean Markdown format, preserving speaker labels for easy analysis in ChatGPT.

## Usage
```bash
python vtt_converter.py
```

Select a .vtt file when prompted. The cleaned transcript will be saved as *_transcript.md in the same folder.

## Packaging as an App (macOS)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "VTT Converter" vtt_converter.py
```

This creates dist/VTT Converter.app that you can double-click.

