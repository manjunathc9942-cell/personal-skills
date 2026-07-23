import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        # FIXED: Changed self.BASE_URL to APIClient.BASE_URL
        url = f"{APIClient.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{APIClient.BASE_URL}/{endpoint}"
        # Make sure this says requests.post, NOT requests.get!
        return requests.post(url, headers=self.headers, json=data)