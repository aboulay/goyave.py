from entities.screen import Screen


class ScreensManager():
    def __init__(self):
        self.screens_list = []

    def load_screens(self, screens):
        self.screens_list = []

        for screen_data in screens:
            self.screens_list.append(self.generate_screen(screen_data))

    def generate_screen(self, screen_data):
        screen = Screen()
        screen.set_name(screen_data["name"])
        screen.set_url(screen_data["url"])
        screen.set_format(screen_data["format"])
        screen.set_data(screen_data["data"])
        screen.set_main_information(screen_data["main"])
        return screen

    def get_screen_list(self):
        return self.screens_list
