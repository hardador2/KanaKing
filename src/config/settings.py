"""
settings.py


Contains the user-edited settings
for the program
"""
import json


with open("./src/config/settings.json", "r", encoding="utf-8") as f:
    SETTINGS: dict = json.load(f)
    DARK_MODE: bool = SETTINGS["dark_mode"]
    CHEAT_MODE: bool = SETTINGS["cheat_mode"]




def change_settings(darkmode: bool, cheatmode: bool):
    """Adjusts user settings."""
    with open("./src/config/settings.json", "w", encoding="utf-8") as f:
        json.dump({"dark_mode":darkmode, "cheat_mode":cheatmode}, f, indent=4)
