from pathlib import Path
import json

# Project Root
ROOT = Path(__file__).resolve().parent.parent

# Important Directories
ASSETS = ROOT / "assets"
GENERATED = ROOT / "generated"
CONFIG = ROOT / "config"

# Images
PROFILE_IMAGE = ASSETS / "images" / "profile-pic.png"

# Output Files
ASCII_OUTPUT = GENERATED / "ascii.svg"
INFO_CARD_OUTPUT = GENERATED / "info-card.svg"
HEATMAP_OUTPUT = GENERATED / "contrib-heatmap.svg"
README_OUTPUT = ROOT / "README.md"

# Config JSON
PROFILE_JSON = CONFIG / "profile.json"


def load_profile():
    """Load profile.json"""

    with open(PROFILE_JSON, "r", encoding="utf-8") as file:
        return json.load(file)


PROFILE = load_profile()