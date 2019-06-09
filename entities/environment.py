class Environment():
    def __init__(self):
        self.name = ""
        self.screen_list = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_screen_list(self):
        return self.screen_list

    def set_screen_list(self, screen_list):
        self.screen_list = screen_list
