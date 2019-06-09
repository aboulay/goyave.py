from usecases.environment.databuilder import EnvironmentDataBuilder
from presenters.interfaces import IPresenter


class EnvironmentPresenter(IPresenter):
    def __init__(self):
        self.environment_builder = EnvironmentDataBuilder()

    def presents(self, environments):
        environment_output = []
        for environment in environments:
            environment_output.append(self.environment_builder.build(environment))
        return environment_output
