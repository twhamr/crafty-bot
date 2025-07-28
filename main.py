from app.main.api.roles import RoleRequests
from app.main.api.servers import ServerRequests
from app.main.api.users import UserRequests


def main():
    role = RoleRequests()
    server = ServerRequests()
    user = UserRequests()

    print(server.get_server(server_id="11ce2e87-7e19-44d1-b639-ea03a67f8a19"))


if __name__ == "__main__":
    main()