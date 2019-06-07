import requests


class ApiCaller():
    def __init__(self, url):
        self.url = url

    def call(self):
        response = requests.get(self.url)
        return response.json()
