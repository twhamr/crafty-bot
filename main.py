from app.main.api.roles import RoleRequests
from app.main.api.servers import ServerRequests
from app.main.api.users import UserRequests


def main():
    role = RoleRequests()
    server = ServerRequests()
    user = UserRequests()

    print(server.get_server_stats(server_id="67ef8abb-86a5-4d34-bb28-b9b87c16e1ef"))


if __name__ == "__main__":
    main()