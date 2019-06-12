from usecases.environment.manager import EnvironmentsManager
from controllers.interfaces import IController


class EnvironmentController(IController):
    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.reload()

    def reload(self):
        self.environment_manager = EnvironmentsManager(self.configuration_file)

    def get_data(self):
        return self.environment_manager.load_environments()
