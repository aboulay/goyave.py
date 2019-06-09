from usecases.screen.manager import ScreensManager
from usecases.configuration.manager import ConfigurationManager
from entities.environment import Environment


class EnvironmentsManager():
    def __init__(self, configuration_file):
        self.configuration_manager = ConfigurationManager(configuration_file)

    def load_environments(self):
        self.configuration_manager.parse_configuration()
        environment_list = []
        configuration = self.configuration_manager.get_configuration()

        for environment in configuration["environments"]:
            environment_list.append(self.__generate_environment(environment))
        return environment_list

    def __generate_environment(self, environment_data):
        screen_manager = ScreensManager()
        environment = Environment()
        environment.set_name(environment_data["name"])
        screen_manager.load_screens(environment_data["screens"])
        environment.set_screen_list(screen_manager.get_screen_list())
        return environment
