# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Servers ------
class ServerRequests(APIHandler):
    # ------ Method: POST ------
    # Get all servers
    def get_all_servers(self) -> list[dict[str, Any]]:
        """
        Get all servers' data.

        Parameters
        ----------
        none

        Returns
        -------
        list[dict[str, Any]]:
            List of JSON serializable dictionaries containing servers and its data
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
        
        if response['data']:
            return response['data']
        
        return [response]


    # Get a server
    def get_server(self, server_id: str) -> dict[str, Any]:
        """
        Get a server's details

        Parameters
        ----------
        server_id: str
            Unique ID of the server

        Returns
        -------
        dict[str, Any]:
            JSON serializable dictionary of the requested server
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

        if response['data']:
            return response['data']
        
        return response

    
    # Get a server's logs
    def get_server_logs(self, server_id: str, file: bool = False, colors: bool = False,
                        raw: bool = False, html: bool = False):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/logs"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Set query params
        query = {
            "file": file,
            "colors": colors,
            "raw": raw,
            "html": html
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers,
                                    query_params=query)

        return response
    
    
    # Get a server's public data
    def get_server_public_data(self, server_id: str):
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

        if response['data']:
            return response['data']
        
        return response
    

    # Get everyone with internal access to a server
    def get_server_access(self, server_id: str):
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
    def get_all_server_webhooks(self, server_id: str):
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
    def get_webhook(self, server_id: str, webhook_id: int):
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
    def send_server_action(self, server_id: str, action: str):
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
    def send_server_stdin_command(self, server_id: str, command: str):
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