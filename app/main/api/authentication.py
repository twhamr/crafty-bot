# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Authentication ------
class AuthenticationRequests(APIHandler):
    # Log out every single session the token's user has
    def invalidate_sessions(self):
        endpoint = "/auth/invalidate_tokens"

    # Login and get a token
    def login_user(self):
        endpoint = "/auth/login"