from typing import Any
from config_handler import ConfigHandler
import os

def setup_config_file() -> None:
    if not os.path.exists(path="./config/main.ini"):
        ConfigHandler(config_path="./config/main.ini").sync()
        print("Config file created")
    else:
        print("Config file already exists")