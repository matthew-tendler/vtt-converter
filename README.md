# VTT Converter 🎙️➡️📄

A small, focused Python utility for converting Zoom `.vtt` transcript files into clean Markdown transcripts while preserving speaker labels.

This project provides a simple graphical interface (Tkinter) to select a `.vtt` file and produce a Markdown file that is easier to read, share, and feed into summarization tools.

---

## Table of contents

- Features
- Requirements
- Installation
- Usage
  - GUI
  - Programmatic (import)
- Output format
- Troubleshooting
- Contributing
- License

---

## ✨ Features

- Converts Zoom `.vtt` files to readable Markdown
- Preserves speaker labels in bold (e.g. **Speaker:** text)
- Saves output next to the original file, with `_transcript.md` suffix
- Small, dependency-light Python implementation

## Requirements

- Python 3.8+
- tkinter (standard with many Python installs; on some systems you may need to install system package)
- Optional: packages listed in `requirements.txt` (this repo includes `pandas`, `pyinstaller`, and `tk` in the requirements file but the converter itself does not require pandas)

If you rely on `requirements.txt`, install via pip as shown below.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/matthew-tendler/vtt-converter.git
cd vtt-converter
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies (optional):

```bash
pip install -r requirements.txt
```

Note: On macOS, if Tkinter is not available you may need to install a Tcl/Tk distribution (for example via Homebrew) and ensure your Python is linked against it. Using the system Python or a Python from Homebrew that includes Tk may help.

---

## Usage

Two common ways to use this project:

### 1) GUI (quick and easy)

Run the script and use the file picker to choose a `.vtt` file:

```bash
python vtt_converter.py
```

After selecting a file the script will write a Markdown transcript in the same folder as the source `.vtt` named `<original>_transcript.md` and show a small dialog with the output path.

### 2) Programmatic (call from code)

You can import the converter function in your own Python code and call it directly:

```python
from vtt_converter import vtt_to_markdown

output_path = vtt_to_markdown("/path/to/meeting.vtt")
print("Saved:", output_path)
```

This returns the output file path so you can wire the result into downstream processing (summarizers, uploaders, etc.).

---

## Output format

- The output file is Markdown with a top-level heading `# Meeting Transcript`.
- Speaker lines are converted to `**Speaker:** text  ` (two spaces at line end to force a Markdown line break where appropriate).
- The output file is saved as `<original_basename>_transcript.md` in the same folder as the `.vtt` file.

## Troubleshooting

- Tkinter / GUI issues on macOS:
  - If running `python vtt_converter.py` raises a `tkinter` import error, install Tcl/Tk (for example `brew install tcl-tk`) and ensure your Python is linked against it. Using the system Python or a Python from Homebrew that includes Tk may help.
- Character encoding issues:
  - The script opens files with `utf-8` encoding. If your `.vtt` contains other encodings, convert to UTF-8 first or modify the script to use the correct encoding.
- Incorrect speaker detection:
  - The script heuristically treats any line containing a colon (`Speaker: text`) as a speaker-labeled line. If your `.vtt` uses a different format you may need to adjust `vtt_converter.py` to suit your transcripts.

## Contributing

Contributions are welcome. A few suggestions:

- Improve speaker detection and handle more `.vtt` variants
- Add command-line flags to allow specifying output filenames or disabling the GUI
- Add unit tests and CI

To contribute:

1. Fork the repository
2. Create a branch for your feature/fix
3. Open a pull request with a clear description of changes

---

## License

No license file is included in this repository. Add a `LICENSE` (for example the MIT license) to make reuse terms explicit.

---

## Contact

If you have questions or feature requests, open an issue on the repository or contact the maintainer.
