import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def vtt_to_markdown(vtt_path):
    # Save output in same folder, but as .md
    folder = os.path.dirname(vtt_path)
    base = os.path.splitext(os.path.basename(vtt_path))[0]
    output_path = os.path.join(folder, base + "_transcript.md")

    lines = []
    with open(vtt_path, "r", encoding="utf-8") as f:
        for line in f:
            # Skip WEBVTT headers, numbers, and raw timestamps
            if re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}", line):
                continue
            if line.strip().lower().startswith("webvtt"):
                continue
            if line.strip().isdigit():
                continue

            clean = line.strip()
            if clean:
                lines.append(clean)

    # Rebuild transcript, preserving speaker labels
    md_lines = ["# Meeting Transcript\n"]
    for l in lines:
        if ":" in l:  # likely a speaker line
            parts = l.split(":", 1)
            speaker = parts[0].strip()
            text = parts[1].strip()
            md_lines.append(f"**{speaker}:** {text}  ")
        else:
            md_lines.append(l + "  ")

    text = "\n".join(md_lines)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(text)

    return output_path

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a Zoom .vtt transcript",
        filetypes=[("VTT files", "*.vtt")]
    )

    if not file_path:
        return

    output = vtt_to_markdown(file_path)
    messagebox.showinfo("Done", f"Transcript saved to:\n{output}")

if __name__ == "__main__":
    main()