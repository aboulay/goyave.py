class Screen():
    def __init__(self):
        self.name = ""
        self.url = ""
        self.format = ""
        self.data = []
        self.main_information = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_main_information(self):
        return self.main_information

    def set_main_information(self, main_information):
        self.main_information = main_information
