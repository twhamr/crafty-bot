# ------ Libraries ------
import os

from app.main.handlers.log_handler import LogHandler


# ------ Handler: Files ------
class FileHandler:
    def __init__(self) -> None:
        self.logger = LogHandler()
    

    def check_directory(self, dir: str) -> bool:
        """
        Check if a directory exists, creates it if not

        Parameters
        ----------
        dir: str
            Path for directory
        
        Returns
        -------
        output: bool
            Success/Failure
        """
        if os.path.exists(path=dir):
            self.logger.create_log(category="system", message=f"INFO: directory [{dir}] already exists")
            return True
        else:
            try:
                os.makedirs(name=dir)
                self.logger.create_log(category="system", message=f"INFO: successfully created directory [{dir}]")
                return True
            except Exception as e:
                self.logger.create_log(category="system", message=f"ERROR: [{e}] | failed to create directory [{dir}]")
                return False