# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Roles ------
class RoleRequests(APIHandler):
    # Get all the roles
    def get_all_roles(self, ids: str = "false") -> dict[str, Any]:
        """
        Get all roles

        Parameters
        ----------
        ids: str, optional
            Return only role IDs [default="false"]

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = "/roles"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Set query params
        query = {
            "ids": ids
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers,
                                    query_params=query)
        
        return response
    
    # Get a role
    def get_role(self, role_id: int) -> dict[str, Any]:
        """
        Get a specified role

        Parameters
        ----------
        role_id: int
            Unique ID for the role

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/roles/{role_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)
        
        return response

    # Get a role's servers
    def get_role_servers(self, role_id: int, ids: str = "false") -> dict[str, Any]:
        """
        Get a role's servers

        Parameters
        ----------
        role_id: int
            Unique ID for the role
        ids: str, optional
            Return only role IDs [default="false"]

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/roles/{role_id}/servers"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Set query params
        query = {
            "ids": ids
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers,
                                    query_params=query)
        
        return response

    # Get a role's users
    def get_role_users(self, role_id: int) -> dict[str, Any]:
        """
        Get a role's users

        Parameters
        ----------
        role_id: int
            Unique ID for the role

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/roles/{role_id}/users"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)
        
        return response