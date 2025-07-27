from app.main.api.roles import RoleRequests
from app.main.api.servers import ServerRequests
from app.main.api.users import UserRequests


def main():
    role = RoleRequests()
    server = ServerRequests()
    user = UserRequests()

    #print(role.get_all_roles(ids="true"))


if __name__ == "__main__":
    main()