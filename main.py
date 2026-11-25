"""make.fun news-image entry: writes the image that sums up Tuesday 24 November 2026's world news.

The image (entry.png beside this file) is rendered by src/build.py from src/stories.py and src/art.py;
this program only copies its bytes, so both runs write the same file and need no network.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).resolve().parent / "entry.png", out_dir / "entry.png")
