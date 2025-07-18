from app.main.classes.api.servers import ServerRequests
from app.main.handlers.config_handler import ConfigHandler

def main():
    # TODO: refactor project to remove database and only use config file
    config = ConfigHandler()

    config.setup_main_config()

    #servers = ServerRequests()

    #print(servers.get_all_servers())
    #print(servers.get_server(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19"))
    #servers.get_server_logs(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_public_data(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_stats(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_access(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_all_server_webhooks(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_webhook(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19", webhook_id=1)


if __name__ == "__main__":
    main()