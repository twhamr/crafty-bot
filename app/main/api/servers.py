# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Servers ------
class ServerRequests(APIHandler):
    # ------ Method: POST ------
    # Get all servers
    def get_all_servers(self) -> dict[str, Any]:
        """
        Get all servers' data.

        Parameters
        ----------
        none

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = "/servers"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)
        
        return response


    # Get a server
    def get_server(self, server_id: str) -> dict[str, Any]:
        """
        Get a server's details

        Parameters
        ----------
        server_id: str
            Unique ID for the server

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    
    # Get a server's logs
    def get_server_logs(self, server_id: str, file: bool = False, colors: bool = False,
                        raw: bool = False, html: bool = False) -> dict[str, Any]:
        """
        Get a server's logs

        Parameters
        ----------
        server_id: str
            Unique ID for the server
        file: bool, optional
            Whether to read the log file or stdout [default=False]
        colors: bool, optional
            Whether to add HTML coloring or not [default=False]
        raw: bool, optional
            Whether to disable ANSI stripping or not [default=False]
        html: bool, optional
            Whether to output in HTML [default=False]
        
        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/logs"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Set query params
        query = {}

        if file:
            query['file'] = "true"
        if colors:
            query['colors'] = "true"
        if raw:
            query['raw'] = "true"
        if html:
            query['html'] = "true"

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers,
                                    query_params=query)

        return response
    
    
    # Get a server's public data
    def get_server_public_data(self, server_id: str) -> dict[str, Any]:
        """
        Get a server's public data

        Parameters
        ----------
        server_id: str
            Unique ID for the server

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/public"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response
    

    # Get a server's statistics
    def get_server_stats(self, server_id: str) -> dict[str, Any]:
        """
        Get a server's stats

        Parameters
        ----------
        server_id: str
            Unique ID for the server

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/stats"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response
    

    # Get everyone with internal access to a server
    def get_server_access(self, server_id: str) -> dict[str, Any]:
        """
        Get users who have internal access to a server

        Parameters
        ----------
        server_id: str
            Unique ID for the server

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/users"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response


    # Get all server webhooks
    def get_all_server_webhooks(self, server_id: str) -> dict[str, Any]:
        """
        Get a server's webhooks

        Parameters
        ----------
        server_id: str
            Unique ID for the server

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/webhook/"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response


    # Get webhook
    def get_webhook(self, server_id: str, webhook_id: int) -> dict[str, Any]:
        """
        Get a server's details

        Parameters
        ----------
        server_id: str
            Unique ID for the server
        webhook_id: int
            Unique ID for the webhook

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/webhook/{webhook_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response
    

    # ------ Method: POST ------
    # Send an action to a server
    # Actions = ["clone_server", "start_server", "stop_server", "restart_server", "kill_server", "backup_server", "update_executable"]
    def send_server_action(self, server_id: str, action: str) -> dict[str, Any]:
        """
        Send an action to a server  
        ["clone_server", "start_server", "stop_server", "restart_server", "kill_server", "backup_server", "update_executable"]

        Parameters
        ----------
        server_id: str
            Unique ID of the server
        action: str
            Action to perform

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/action/{action}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers)

        return response


    # Send a STDIn command to a server
    def send_server_stdin_command(self, server_id: str, command: str) -> dict[str, Any]:
        """
        Send a Minecraft command to a server

        Parameters
        ----------
        server_id: str
            Unique ID of the server
        command: str
            Command to execute

        Returns
        -------
        response: dict[str, Any]
            HTTP request response
        """
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/stdin"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers,
                                     body=command)

        return response