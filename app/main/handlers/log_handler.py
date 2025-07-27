from typing import Any
from datetime import datetime
import json

from app.main.handlers.config_handler import ConfigHandler
from app.main.handlers.file_handler import FileHandler

class LogHandler(FileHandler):
    def __init__(self) -> None:
        self.config = ConfigHandler()

        logs = self.config.read_config(section="logging")

        self.log_root_path = logs['root_path']


    def create_log(self, category: str, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = timestamp[:10]
        
        #print(f"[{timestamp}] [{category}] {message}")
        self.save_log(category=category, filename=f"{date}-{category}.log", log=f"[{timestamp}] [{category}] {message}")

    def save_log(self, category: str, filename: str, log: str) -> None:
        file_path = f"{self.log_root_path}/{self.normalize_filename(filename=filename)}"

        with open(file=file_path, mode="a") as log_file:
            log_file.write(log + "\n")