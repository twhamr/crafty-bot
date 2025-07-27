# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Authentication ------
class AuthenticationRequests(APIHandler):
    # Log out every single session the token's user has
    def invalidate_sessions(self) -> dict[str, Any]:
        # Set endpoint for API call
        endpoint = "/auth/invalidate_tokens"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers)
        
        return response

    # Login and get a token
    # BUG: API call cannot authorize user if MFA is active
    def login_user(self) -> dict[str, Any]:
        # Set endpoint for API call
        endpoint = "/auth/login"

        # Set headers for request
        headers = {
            "Content-Type": "application/json"
        }

        # Set request body
        request = {
            "username": self.username,
            "password": self.password
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers,
                                     json_request=request)
        
        if response['data']:
            return response['data']
        
        return response