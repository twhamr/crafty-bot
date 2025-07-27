from app.main.api.roles import RoleRequests
from app.main.api.servers import ServerRequests
from app.main.api.users import UserRequests


def main():
    role = RoleRequests()
    server = ServerRequests()
    user = UserRequests()

    #print(user.get_user_public_data(user_id=1))


if __name__ == "__main__":
    main()