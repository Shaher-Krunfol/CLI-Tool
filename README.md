# 🛠 Log Inspector CLI Tool

A Python CLI tool that **scans log files**, filters out lines with **errors** and **warnings**, extracts **timestamps**, and generates a clear **summary**.  
Currently includes both a **Beginner Version** and an **Intermediate Version** – with a more **Advanced Version** in the works.

---

## 📌 Features

### ✅ Beginner Version
- Reads a log file and scans each line for the words **“error”** and **“warning.”**
- Prints all matching lines, their line numbers, and a count.
- Detects and prints **first** and **last timestamps** in the file.
- Optionally saves the filtered lines into a file.

> 💡 Perfect for **beginners** learning about Python basics like file handling, loops, and exception handling.

---

### 🚀 Intermediate Version (Current Main Release)
- Fully **OOP-based** (clean class design using `LogParser`).
- Uses **command-line arguments** via `argparse` — no more typing filenames manually.
- Supports:
  - `--save` → Automatically saves results without asking.
  - `--errors-only` → Filters only “error” lines (ignores warnings).
  - `--output` → Lets you pick a custom save filename.
- Cleaner, **PEP8-compliant** code and structured summary output.
- Graceful error handling for missing files, empty logs, and permission issues.

> ✅ This version is great for **practicing real-world coding structure**, CLI tools, and reusable class methods.

---
🔥 Advanced Version (✅ Completed)

The Advanced Version of the Log Inspector CLI Tool is now here! 🚀

✅ What’s new:

    Streaming support: Uses Python generators to process massive log files (1GB+ tested) in seconds without loading the whole file into memory.

    Flexible log-level filtering: Use --levels to extract only the messages you care about (e.g., ERROR, WARNING, INFO).

    Clean summary output: No clutter in your terminal – all matches are saved to a file.

    Safe & robust: Handles missing files, permission errors, and works on any text-based log file.

✅ Example usage:

python log_parser.py server.log /
python log_parser.py server.log --levels ERROR,INFO /
python log_parser.py server.log --levels WARNING --output warnings.txt

✅ Performance:
Tested on a 1 GB log file – filtered all matching lines in ~5-10 seconds.

