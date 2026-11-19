"""News image for 19 November 2026 — writes entry.png to /output."""
import shutil, os
from pathlib import Path

here = Path(__file__).parent
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copy2(here / "entry.png", out / "entry.png")
print(f"Wrote {out / 'entry.png'}")
