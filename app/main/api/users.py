# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Users ------
class UserRequests(APIHandler):
    # ------ Method: GET ------
    # Get all the users
    def get_all_users(self) -> dict[str, Any]:
        """
        Get all users

        Parameters
        ----------
        none

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = "/users"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    # Get a user
    def get_user(self, user_id: int) -> dict[str, Any]:
        """
        Get a specific user

        Parameters
        ----------
        user_id: int
            Unique ID for the user

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/users/{user_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    # Get a user's Crafty permissions
    def get_user_permissions(self, user_id: int) -> dict[str, Any]:
        """
        Get a user's permissions

        Parameters
        ----------
        user_id: int
            Unique ID for the user

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/users/{user_id}/permissions"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    # Get a user's profile picture
    def get_user_picture(self, user_id: int) -> dict[str, Any]:
        """
        Get a user's profile picture

        Parameters
        ----------
        user_id: int
            Unique ID for the user

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/users/{user_id}/pfp"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    # Get a user's public data
    def get_user_public_data(self, user_id: int) -> dict[str, Any]:
        """
        Get a user's public data

        Parameters
        ----------
        user_id: int
            Unique ID for the user

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/users/{user_id}/public"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response