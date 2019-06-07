from usecases.configuration.manager import ConfigurationManager
from usecases.api.manager import ApiManager


class Orchestrator():
    def __init__(self, configuration_file):
        self.configuration_manager = ConfigurationManager(configuration_file)

    def update_configuration(self):
        self.configuration_manager.parse_configuration()

    def update_api_manager_list(self):
        configuration = self.configuration_manager.get_configuration()
        self.api_managers = []

        for api in configuration['targets']:
            self.api_managers.append(ApiManager(api['name'], api['url']))

    def get_api_manager_list(self):
        return self.api_managers
