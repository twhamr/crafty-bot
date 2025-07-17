from typing import Any
from datetime import datetime, timezone
import json

from handlers.file_handler import FileHandler

class LogHandler:
    def __init__(self) -> None:
        self.files = FileHandler()


    def create_log(self, location: str, message: str) -> None:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        date = timestamp[:10]
        
        print(f"[{timestamp}] [{location}] {message}")
        self.files.save_log(location=location, filename=f"{date}-{location}.log", log=f"[{timestamp}] [{location}] {message}")