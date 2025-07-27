from typing import Any

from app.main.handlers.api_handler import APIHandler

class JSONRequests(APIHandler):
    # ------ METHOD: GET ------

    # Get all JSON schemas
    def get_all_schemas(self):
        # Set endpoint for API call
        endpoint = "/jsonschema"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response

    # Get a JSON schema
    def get_schema(self, json_name: str):
        # Set endpoint for API call
        endpoint = f"/jsonschema/{json_name}"

        # Set headers for request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make request using given parameters
        response = self.get_request(endpoint=endpoint,
                                    headers=headers)

        return response