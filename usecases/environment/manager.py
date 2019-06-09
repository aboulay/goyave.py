from usecases.configuration.manager import ConfigurationManager
from usecases.screen.manager import ScreensManager
from entities.environment.environment import Environment


class EnvironmentsManager():
    def __init__(self, configuration_file):
        self.configuration_manager = ConfigurationManager(configuration_file)
        self.environment_list = []

    def load_environments(self):
        self.environment_list = []
        self.configuration_manager.parse_configuration()
        configuration = self.configuration_manager.get_configuration()

        environments = []
        for environment in configuration["environments"]:
            environments.append(self.__generate_environment(environment))
        self.environment_list = environments

    def __generate_environment(self, environment_data):
        screen_manager = ScreensManager()
        environment = Environment()
        environment.set_name(environment_data["name"])
        screen_manager.load_screens(environment_data["screens"])
        environment.set_screen_list(screen_manager.get_screen_list())
        return environment

    def get_environment_list(self):
        return self.environment_list
