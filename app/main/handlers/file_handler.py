# ------ Libraries ------
import unicodedata
import os
import re


# ------ Handler: Files ------
class FileHandler:
    @staticmethod
    def normalize_filename(filename: str, max_length: int = 255) -> str:
        """
        Normalize a string to make it safe for use as a filename.

        Args:
            filename (str): The original string to normalize.
            max_length (int): Maximum length of the resulting filename.

        Returns:
            str: A safe, normalized filename.
        """
        # Normalize Unicode to ASCII (e.g., é -> e)
        safe_str = unicodedata.normalize('NFKD', filename)
        safe_str = safe_str.encode('ascii', 'ignore').decode('ascii')

        # Remove forbidden characters on Windows and most filesystems
        safe_str = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', safe_str)

        # Replace whitespace with underscores
        safe_str = re.sub(r'\s+', '_', safe_str)

        # Strip leading/trailing dots or underscores
        safe_str = safe_str.strip('._')

        # Truncate to max length
        safe_str = safe_str[:max_length]

        # Avoid Windows reserved device names (CON, PRN, AUX, NUL, COM1..COM9, LPT1..LPT9)
        reserved = {
            "CON", "PRN", "AUX", "NUL",
            *(f"COM{i}" for i in range(1, 10)),
            *(f"LPT{i}" for i in range(1, 10))
        }
        if safe_str.upper() in reserved:
            safe_str += "_file"

        return safe_str or "default_filename"