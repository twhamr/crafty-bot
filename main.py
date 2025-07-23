from app.main.classes.api.servers import ServerRequests

from app.main.handlers.config_handler import ConfigHandler

def main():
    config = ConfigHandler()
    server = ServerRequests()

    #config.setup_main_config()
    #print(server.get_all_servers())
    #print(server.get_server_stats(server_id="6b84b5e5-7e7d-47cd-8d55-d7597b789d4f"))


if __name__ == "__main__":
    main()