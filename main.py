from app.main.api.servers import ServerRequests
from app.main.handlers.config_handler import ConfigHandler


def main():
    config = ConfigHandler()
    server = ServerRequests()

    #print(authentication.invalidate_sessions())
    print(server.get_all_servers())


if __name__ == "__main__":
    main()