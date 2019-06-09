from usecases.configuration.manager import ConfigurationManager
from entities.screen.screen import Screen


class ScreensManager():
    def __init__(self, configuration_file):
        self.configuration_manager = ConfigurationManager(configuration_file)
        self.screens_list = []

    def load_screens(self):
        self.screens_list = []

        self.configuration_manager.parse_configuration()
        configuration = self.configuration_manager.get_configuration()

        for target in configuration["targets"]:
            self.screens_list.append(self.generate_screen(target))

    def generate_screen(self, target):
        screen = Screen()
        screen.set_name(target["name"])
        screen.set_url(target["url"])
        screen.set_format(target["format"])
        screen.set_data(target["data"])
        screen.set_main_information(target["main"])
        return screen

    def get_screen_list(self):
        return self.screens_list
