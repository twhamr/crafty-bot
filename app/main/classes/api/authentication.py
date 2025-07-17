import requests
from typing import Any

from handlers.api_handler import APIHandler

class AuthenticationRequests(APIHandler):
    # Log out every single session the token's user has
    def invalidate_sessions(self):
        pass

    # Login and get a token
    def login_user(self):
        pass