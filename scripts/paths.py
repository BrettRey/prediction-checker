"""Locate a source file: the portfolio's literature/ folder when the repo sits
inside it, otherwise data/raw/sources/ (filled by scripts/fetch_raw.sh)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def source(name):
    for base in (ROOT.parents[2] / "literature", ROOT / "data" / "raw" / "sources"):
        p = base / name
        if p.exists():
            return p
    raise FileNotFoundError(f"{name}: not in literature/ or data/raw/sources/; run scripts/fetch_raw.sh")
