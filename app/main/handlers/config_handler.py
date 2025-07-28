# ------ Libraries ------
from typing import Any
import configparser
import os


# ------ Handler: Configuration ------
class ConfigHandler:
    def __init__(self) -> None:
        self.root_path = "./app/config"
        self.parser = configparser.ConfigParser()


    def setup_main_config(self) -> bool:
        """
        Initialize main.ini

        Returns
        -------
        output: bool
            Whether main.ini was created or not
        """
        if not os.path.exists(path=f"{self.root_path}/main.ini"):
            writer = configparser.ConfigParser()

            self.parser.read(filenames=f"{self.root_path}/main.ini.template")

            template = {}
            for section in self.parser.sections():
                template.update({section: dict(self.parser[section])})
            
            
            for section in template:
                writer[section] = template[section]
            
            try:
                with open(file=f"{self.root_path}/main.ini", mode="w") as file:
                    writer.write(file)

                #self.logger.create_log(category="system", message=f"INFO: successfully created main.ini at {self.root_path}")
                return True
            except Exception as e:
                #self.logger.create_log(category="system", message=f"ERROR: [{e}] | failed to create main.ini")
                return False
        else:
            #self.logger.create_log(category="system", message="ERROR: main.ini exists already")
            return False
    

    def read_config(self, section: str) -> dict[str, Any]:
        """
        Read a section of the configuration file: *main.ini*

        Parameters
        ----------
        section: str
            Configuration section to read
        
        Returns
        -------
        output: dict[str, Any]
            Contents of the section
        """
        self.parser.read(filenames=f"{self.root_path}/main.ini")

        return dict(self.parser[section])