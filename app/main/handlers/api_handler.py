from typing import Any
import requests
import json

from database import Database
from app.handlers.log_handler import LogHandler

class APIHandler:
    def __init__(self) -> None:
        db = Database()

        self.api_key= db.pull_user_key()
        self.host = "https://192.168.1.158:8443/api/v2"
        self.logger = LogHandler()
        self.verify = False


    def get_request(self,
                    endpoint: str,
                    headers: dict[str, Any] = {},
                    query_params: dict[str, Any] = {},
                    json_request: dict[str, Any] = {},
                    body: str = ""):
        
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


    def post_request(self,
                     endpoint: str,
                     headers: dict[str, Any] = {},
                     query_params: dict[str, Any] = {},
                     json_request: dict[str, Any] = {},
                     body: str = ""):
        
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


    def patch_request(self,
                      endpoint: str,
                      headers: dict[str, Any] = {},
                      query_params: dict[str, Any] = {},
                      json_request: dict[str, Any] = {},
                      body: str = ""):
        
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


    def delete_request(self,
                       endpoint: str,
                       headers: dict[str, Any] = {},
                       query_params: dict[str, Any] = {},
                       json_request: dict[str, Any] = {},
                       body: str = ""):
        
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