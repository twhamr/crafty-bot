# ------ Libraries ------
from typing import Any

from app.main.handlers.api_handler import APIHandler


# ------ API: Servers ------
class ServerRequests(APIHandler):
    # ------ METHOD: GET ------

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
        response = self.get_request(endpoint=endpoint, headers=headers)

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
    

    # ------ METHOD: POST ------

    # Create a server
    # JSON schema: new_server
    # BUG: new server is successful; however, API returns a 501 error saying executable_update_url does not exist
    # documentation does not show where to place the url...
    def create_server(self, name: str, roles: list[int], stop_command : str = "", log_location: str = "", crashdetection: bool = False,
                      autostart: bool = False, autostart_delay: int = 10, monitoring_type: str = "minecraft_java", host: str = "127.0.0.1", port: int = 25565,
                      create_type: str = "minecraft_java", java_type: str = "vanilla", java_version: str = "1.21.7", mem_min: int = 1, mem_max: int = 2,
                      server_properties_port: int = 25565, agree_to_eula: bool = True):
        """
        Create a new server.

        Parameters
        ----------
        name : str
            Name for server
            -> examples: ["Test API Server", "Minecraft Vanilla Server"]
        
        roles : array
            Roles to add
            -> examples: [1, 2]

        stop_command : str, default=""
            Stop command ("" means the default for the server creation type.)
            -> examples: ["stop", "end"]

        log_location : str, default=""
            Log file ("" means the default for the server creation type.)
            -> examples: ["./logs/latest.log", "./proxy.log.0"]

        crashdetection : bool, default=False
            Detect if server crashes
            -> either True or False

        autostart : bool, default=False
            If true, the server will be started automatically when Crafty is launched
            -> either True or False
        
        autostart_delay : int, default=10
            Delay in seconds before autostarting (if enabled)
            -> minimum: 0
        
        monitoring_type : str, default="minecraft_java"
            Server monitoring type
            -> select: ["minecraft_java", "minecraft_bedrock", "none"]
        
        host : str, default="127.0.0.1"
            Monitoring host
            -> examples: ["127.0.0.1"]
        
        port : int, default=25565
            Monitoring port ("minecraft_java" = 25565; "minecraft_bedrock" = 19132)
            -> examples: [25565, 19132]

        create_type : str, default="minecraft_java"
            Server creation type
            -> select: ["minecraft_java", "minecraft_bedrock"]
        
        java_type : str, default="vanilla"
            Server JAR type (if creation_type="minecraft_java")
            -> select: ["vanilla", "paper", "fabric", "folia", "forge-installer", "neoforge-installer", "purpur"]
        
        java_version : str, default="1.21.7"
            Server JAR version (if creation_type="minecraft_java")
            -> examples: ["1.21.7", "1.18.2", "1.12.2", etc.]
        
        mem_min : int, default=1
            Minimum JVM memory (in GiBs) (if creation_type="minecraft_java")
            -> examples: [1, 2, 3, 4]
        
        mem_max : int, default=2
            Maximum JVM memory (in GiBs) (if creation_type="minecraft_java")
            -> examples: [1, 2, 3, 4]
        
        server_properties_port : int, default=25565
            Server port (if creation_type="minecraft_java")
            -> examples: [25565]
        
        agree_to_eula : bool, default=True
            Agree to the EULA
            -> either True or False

        """
        # Set endpoint for API call
        endpoint = "/servers"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        schema = {
            "name": name,
            "roles": roles,
            "stop_command": stop_command,
            "log_location": log_location,
            "crashdetection": crashdetection,
            "autostart": autostart,
            "autostart_delay": autostart_delay,
            "monitoring_type": monitoring_type,
            "create_type": create_type
        }

        assert monitoring_type in ["minecraft_java", "minecraft_bedrock"], "Value not in ['minecraft_java', 'minecraft_bedrock']"
        if monitoring_type == "minecraft_java":
            schema['minecraft_java_monitoring_data'] = {
                "host": host,
                "port": port
            }
        elif monitoring_type == "minecraft_bedrock":
            schema['minecraft_bedrock_monitoring_data'] = {
                "host": host,
                "port": port
            }

        assert create_type in ["minecraft_java", "minecraft_bedrock"], "Value not in ['minecraft_java', 'minecraft_bedrock']"
        if create_type == "minecraft_java":
            schema['minecraft_java_create_data'] = {
                "create_type": "download_jar",
                "download_jar_create_data": {
                    "category": "Mc_java_servers",
                    "type": java_type,
                    "version": java_version,
                    "mem_min": mem_min,
                    "mem_max": mem_max,
                    "server_properties_port": server_properties_port,
                    "agree_to_eula": agree_to_eula
                }
            }
        elif create_type == "minecraft_bedrock":
            schema['minecraft_bedrock_create_data'] = {
                "create_type": "download_exe",
                "download_exe_create_data": {
                    "agree_to_eula": agree_to_eula
                }
            }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers,
                                     json_request=schema)

        return response


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


    # Create a schedule for a server
    # JSON schema: new_task
    # TODO: untested
    def create_schedule(self, server_id: str, schedule_data: dict[str, Any]):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/tasks/"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers,
                                     json_request=schedule_data)

        return response
    

    # Create a server webhook
    # JSON schema: create_webhook
    # TODO: untested
    def create_server_webhook(self, server_id: str, webhook_data: dict[str, Any]):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/webhook/"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers,
                                     json_request=webhook_data)

        return response


    # Test a server webhook
    # TODO: untested
    def test_server_webhook(self, server_id: str, webhook_id):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/webhook/{webhook_id}/"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.post_request(endpoint=endpoint,
                                     headers=headers)

        return response


    # ------ METHOD: PATCH ------

    # Modify a server
    # JSON schema: server_patch
    # TODO: untested
    def modify_server(self, server_id: str, patch: dict[str, Any]):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.patch_request(endpoint=endpoint,
                                      headers=headers,
                                      json_request=patch)

        return response


    # Modify a schedule for a server
    # JSON schema: patch_task
    # TODO: untested
    def modify_schedule(self, server_id: str, task_id, patch: dict[str, Any]):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/tasks/{task_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.patch_request(endpoint=endpoint,
                                      headers=headers,
                                      json_request=patch)

        return response


    # Modify a server webhook
    # JSON schema: patch_webhook
    # TODO: untested
    def modify_server_webhook(self, server_id: str, webhook_id, patch: dict[str, Any]):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/tasks/{webhook_id}/"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.patch_request(endpoint=endpoint,
                                      headers=headers,
                                      json_request=patch)

        return response


    # ------ METHOD: DELETE ------

    # Delete a server
    # TODO: untested
    def delete_server(self, server_id: str):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.delete_request(endpoint=endpoint,
                                       headers=headers)

        return response
    

    # Delete a schedule
    # TODO: untested
    def delete_schedule(self, server_id: str, task_id):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/tasks/{task_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.delete_request(endpoint=endpoint,
                                       headers=headers)

        return response
    
    
    # Delete webhook
    # TODO: untested
    def delete_webhook(self, server_id: str, webhook_id):
        # Set endpoint for API call
        endpoint = f"/servers/{server_id}/webhook/{webhook_id}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.delete_request(endpoint=endpoint,
                                       headers=headers)

        return response