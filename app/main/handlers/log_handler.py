# ------ Libraries ------
from datetime import datetime
import pytz

from app.main.handlers.config_handler import ConfigHandler


# ------ Handler: Logging ------
class LogHandler:
    def __init__(self) -> None:
        self.config = ConfigHandler()

        logs = self.config.read_config(section="logging")

        self.log_root_path = logs['root_path']
        self.enabled = logs['enabled'].lower()
        self.timezone = logs['timezone']


    def create_log(self, category: str, message: str) -> None:
        if self.timezone == "system":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            override = pytz.timezone(self.timezone)
            timestamp = datetime.now(override).strftime("%Y-%m-%d %H:%M:%S")

        date = timestamp[:10]
        
        if self.enabled == "true":
            self.save_log(filename=f"{date}-{category}.log", log=f"[{timestamp}] [{category}] {message}")
        else:
            print(f"[{timestamp}] [{category}] {message}")

    def save_log(self, filename: str, log: str) -> None:
        file_path = f"{self.log_root_path}/{filename}"

        with open(file=file_path, mode="a") as log_file:
            log_file.write(log + "\n")