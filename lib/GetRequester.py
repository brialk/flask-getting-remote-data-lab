import requests
import json

class GetRequester:
    """A reusable class that fetches data from a URL and converts JSON responses into Python data."""
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to the stored URL and return the raw response content."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Fetch the raw response and convert it from JSON text into a Python list/dictionary."""
        response_body = self.get_response_body()
        return json.loads(response_body)