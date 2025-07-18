from typing import Any
import configparser
import os

from app.main.handlers.file_handler import FileHandler

class ConfigHandler(FileHandler):
    def __init__(self) -> None:
        self.config_root_path = "./config"
        self.parser = configparser.ConfigParser()


    def setup_main_config(self) -> None:
        if not os.path.exists(path=f"{self.config_root_path}/main.ini"):
            writer = configparser.ConfigParser()

            self.parser.read(filenames=f"{self.config_root_path}/main.ini.template")

            template = {}
            for section in self.parser.sections():
                template.update({section: dict(self.parser[section])})
            
            
            for section in template:
                writer[section] = template[section]

            with open(file=f"{self.config_root_path}/main.ini", mode="w") as file:
                writer.write(file)

            #print("Config file created")
        else:
            print("Config file already exists")
    

    def read_api(self) -> dict[str, Any]:
        self.parser.read(filenames=f"{self.config_root_path}/main.ini")

        return dict(self.parser['api'])


    def read_discord(self) -> dict[str, Any]:
        self.parser.read(filenames=f"{self.config_root_path}/main.ini")

        return dict(self.parser['discord'])


    def read_logging(self) -> dict[str, Any]:
        self.parser.read(filenames=f"{self.config_root_path}/main.ini")

        return dict(self.parser['logging'])