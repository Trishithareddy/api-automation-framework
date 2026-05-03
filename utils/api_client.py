import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}", timeout=10)

    def post(self, endpoint, payload):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=payload, timeout=10)

    def put(self, endpoint, payload):
        return requests.put(f"{self.BASE_URL}{endpoint}", json=payload, timeout=10)

    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}", timeout=10)
