from datasources.api.api_caller import ApiCaller


class ApiManager():
    def __init__(self, name, api_url):
        self.name = name
        self.url = api_url
        self.api_caller = ApiCaller(api_url)

    def call_api(self):
        return self.api_caller.call()

    def dump(self):
        return {"name": self.name, "url": self.url}
