from typing import Any
import requests
import json

from app.main.handlers.config_handler import ConfigHandler
from app.main.handlers.log_handler import LogHandler

class APIHandler:
    def __init__(self) -> None:
        self.config = ConfigHandler()
        self.logger = LogHandler()

        api = self.config.read_api()

        self.username = api['username']
        self.password = api['password']
        self.api_key= api['api_key']
        self.host = api['api_url']        
        self.verify = False


    def get_request(self,
                    endpoint: str,
                    headers: dict[str, Any] = {},
                    query_params: dict[str, Any] = {},
                    json_request: dict[str, Any] = {},
                    body: str = "") -> dict[str, Any]:
        
        # Make the HTTP request
        response = requests.get(url=(self.host + endpoint),
                                headers=headers,
                                params=query_params,
                                json=json_request,
                                data=body,
                                verify=self.verify)
        
        # If response returns successful
        if response.status_code == 200:
            self.logger.create_log(location="api",
                                   message=f"{response.status_code} OK: successful response | endpoint={endpoint}")
            
            return response.json()
        # If there was an error [400, 401, etc.]
        else:
            error = response.json()

            self.logger.create_log(location="api",
                    message=f"{response.status_code} Error: {response.reason} | reason={error['error']} | details={error['error_data']}")
            
            return error


    def post_request(self,
                     endpoint: str,
                     headers: dict[str, Any] = {},
                     query_params: dict[str, Any] = {},
                     json_request: dict[str, Any] = {},
                     body: str = "") -> dict[str, Any]:
        
        # Make the HTTP request
        response = requests.post(url=(self.host + endpoint),
                                 headers=headers,
                                 params=query_params,
                                 json=json_request,
                                 data=body,
                                 verify=self.verify)
        
        # If response returns successful
        if response.status_code == 200:
            self.logger.create_log(location="api",
                                   message=f"{response.status_code} OK: successful response | endpoint={endpoint}")

            return response.json()
        # If there was an error [400, 401, etc.]
        else:
            error = response.json()

            self.logger.create_log(location="api",
                    message=f"{response.status_code} Error: {response.reason} | reason={error['error']} | details={error['error_data']}")
            
            return error


    def patch_request(self,
                      endpoint: str,
                      headers: dict[str, Any] = {},
                      query_params: dict[str, Any] = {},
                      json_request: dict[str, Any] = {},
                      body: str = "") -> dict[str, Any]:
        
        # Make the HTTP request
        response = requests.patch(url=(self.host + endpoint),
                                 headers=headers,
                                 params=query_params,
                                 json=json_request,
                                 data=body,
                                 verify=self.verify)
        
        # If response returns successful
        if response.status_code == 200:
            self.logger.create_log(location="api",
                                   message=f"{response.status_code} OK: successful response | endpoint={endpoint}")

            return response.json()
        # If there was an error [400, 401, etc.]
        else:
            error = response.json()

            self.logger.create_log(location="api",
                    message=f"{response.status_code} Error: {response.reason} | reason={error['error']} | details={error['error_data']}")
            
            return error


    def delete_request(self,
                       endpoint: str,
                       headers: dict[str, Any] = {},
                       query_params: dict[str, Any] = {},
                       json_request: dict[str, Any] = {},
                       body: str = "") -> dict[str, Any]:
        
        # Make the HTTP request
        response = requests.delete(url=(self.host + endpoint),
                                   headers=headers,
                                   params=query_params,
                                   json=json_request,
                                   data=body,
                                   verify=self.verify)
        
        # If response returns successful
        if response.status_code == 200:
            self.logger.create_log(location="api",
                                   message=f"{response.status_code} OK: successful response | endpoint={endpoint}")

            return response.json()
        # If there was an error [400, 401, etc.]
        else:
            error = response.json()

            self.logger.create_log(location="api",
                    message=f"{response.status_code} Error: {response.reason} | reason={error['error']} | details={error['error_data']}")
            
            return error