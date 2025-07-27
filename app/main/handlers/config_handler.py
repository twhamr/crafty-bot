from typing import Any
import configparser
import os

from app.main.handlers.file_handler import FileHandler

class ConfigHandler(FileHandler):
    def __init__(self) -> None:
        self.root_path = "./app/config"
        self.parser = configparser.ConfigParser()


    def setup_main_config(self) -> None:
        if not os.path.exists(path=f"{self.root_path}/main.ini"):
            writer = configparser.ConfigParser()

            self.parser.read(filenames=f"{self.root_path}/main.ini.template")

            template = {}
            for section in self.parser.sections():
                template.update({section: dict(self.parser[section])})
            
            
            for section in template:
                writer[section] = template[section]

            with open(file=f"{self.root_path}/main.ini", mode="w") as file:
                writer.write(file)

            #print("Config file created")
        else:
            print("Config file already exists")
    

    def read_config(self, section: str) -> dict[str, Any]:
        self.parser.read(filenames=f"{self.root_path}/main.ini")

        return dict(self.parser[section])