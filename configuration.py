import os
from typing import Final

MOBILE_DEVICES = {
    'samsung': 'Galaxy S9+',
    'default': 'Nexus 7',
}

TWITCH_MOBILE_URL: Final[str] = "https://m.twitch.tv"
LANGUAGE = 'en'

PROJECT_ROOT: Final[str] = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR: Final[str] = os.path.join(PROJECT_ROOT, "screenshots")
