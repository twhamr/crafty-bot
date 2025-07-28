# ------ Libraries ------
import os


# ------ Handler: Files ------
class FileHandler:
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
            
            return True
        else:
            try:
                os.makedirs(name=dir)
                
                return True
            except:
                
                return False