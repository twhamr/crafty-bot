from typing import Any
from datetime import datetime, timezone
import json

from app.main.handlers.config_handler import ConfigHandler
from app.main.handlers.file_handler import FileHandler

class LogHandler(FileHandler):
    def __init__(self) -> None:
        self.config = ConfigHandler()

        logs = self.config.read_logging()

        self.log_root_path = logs['root_path']


    def create_log(self, location: str, message: str) -> None:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        date = timestamp[:10]
        
        print(f"[{timestamp}] [{location}] {message}")
        self.files.save_log(location=location, filename=f"{date}-{location}.log", log=f"[{timestamp}] [{location}] {message}")

    def save_log(self, location: str, filename: str, log: str) -> None:
        file_path = f"{self.log_root_path}/{location}/{self.normalize_filename(filename=filename)}"

        with open(file=file_path, mode="a") as log_file:
            log_file.write(log + "\n")