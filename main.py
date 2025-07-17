from app.main.classes.api.servers import ServerRequests


def main():
    servers = ServerRequests()

    print(servers.get_all_servers())
    print(servers.get_server(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19"))
    #servers.get_server_logs(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_public_data(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_stats(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_server_access(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_all_server_webhooks(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19")
    #servers.get_webhook(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19", webhook_id=1)


if __name__ == "__main__":
    main()