from config.config import DevConfig, ProdConfig
import requests

# DataIngestor class handles fetching competition data from the football-data API.
class DataIngestor:
    def __init__(self, config_class=DevConfig):
        # Initialize with configuration class (DevConfig or ProdConfig)
        self.competitions_url = config_class.competitions_url
        self.headers = config_class.headers


    def fetch_competitions(self):
        """
        Fetches competition data from the API endpoint.
        Returns the JSON response if successful, otherwise returns None.
        Handles HTTP errors and general exceptions.
        """
        try:
            # Make GET request to the competitions endpoint
            response = requests.get(self.competitions_url, headers=self.headers)
            # Raise an exception for HTTP error codes
            response.raise_for_status()
            # Return the JSON response if successful
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 404, 500)
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            # Handle any other exceptions
            print(f"An error occurred: {err}")
            return None