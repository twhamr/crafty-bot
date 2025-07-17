from typing import Any

from handlers.api_handler import APIHandler

class CraftyRequests(APIHandler):
    # ------ METHOD: PATCH ------

    # Modify config.json
    # JSON schema: config_json_schema
    def modify_config(self, patch: dict[str, Any]):
        # Set endpoint for API call
        endpoint = "/crafty/config"

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