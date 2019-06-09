import yaml

from usecases.configuration.exceptions \
    import UnknownConfigurationFileTypeException
from usecases.configuration.exceptions \
    import InvalidConfigurationFileException


class ConfigurationManager():
    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.configuration = []

    def parse_configuration(self):
        configuration = self.read_configuration()
        self.validate_configuration(configuration)
        self.configuration = configuration

    def get_configuration(self):
        return self.configuration

    def read_configuration(self):
        if (self.configuration_file.endswith(".yml") or
                self.configuration_file.endswith(".yaml")):
            return self.__read_yaml_configuration()
        else:
            raise UnknownConfigurationFileTypeException()

    def __read_yaml_configuration(self):
        with open(self.configuration_file, 'r') as stream:
            data = yaml.safe_load(stream)
        return data

    def validate_configuration(self, configuration):
        if not configuration.get('targets'):
            raise InvalidConfigurationFileException()
        for target in configuration['targets']:
            if not target.get('name'):
                raise InvalidConfigurationFileException()
            if not target.get('url'):
                raise InvalidConfigurationFileException()
            if not target.get('format'):
                raise InvalidConfigurationFileException()
            if (not target.get('data') or
                    target['data'] is None):
                raise InvalidConfigurationFileException()
            if not target.get('main'):
                raise InvalidConfigurationFileException()
