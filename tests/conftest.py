import sys
from pathlib import Path

# Add `src` to `sys.path` so `project` can be imported in tests
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
# keep path short enough for flake8
sys.path.insert(0, str(SRC))
