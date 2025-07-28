from app.main.handlers.file_handler import FileHandler
from app.main.handlers.config_handler import ConfigHandler

def main():
    config = ConfigHandler()
    file = FileHandler()

    print("""
==================================================================
                    Welcome to CraftyBot\n
 This file will setup everything needed for CraftyBot to function\n
                   Just sit back and enjoy!
==================================================================
    """)
    # Ensuring directories exist
    print("-> Ensuring required directories exist:")
    if file.check_directory(dir="./app/config"):
        print("SUCCESS: config directory exists")
    else:
        print("ERROR: config directory does not exist, check logs for error")

    if file.check_directory(dir="./app/logs"):
        print("SUCCESS: logs directory exists")
    else:
        print("ERROR: logs directory does not exist, check logs for error")

    # Configuration Setup
    print("-> Running configuration setup:")
    if config.setup_main_config():
        print("SUCCESS: Configuration file has been created")
    else:
        print("ERROR: Configuration file was not created, either it exists already or an error occured")

    


if __name__ == "__main__":
    main()