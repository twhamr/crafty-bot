from app.main.classes.api.servers import ServerRequests
from app.main.handlers.config_handler import ConfigHandler

def main():
    config = ConfigHandler()
    server = ServerRequests()

    #config.setup_main_config()


if __name__ == "__main__":
    main()