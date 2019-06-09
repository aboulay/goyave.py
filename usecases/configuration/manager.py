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
        if not configuration.get('environments'):
            raise InvalidConfigurationFileException()
        for environment in configuration['environments']:
            if not environment.get('name'):
                raise InvalidConfigurationFileException()
            if not environment.get('screens'):
                raise InvalidConfigurationFileException()
            for screen in environment['screens']:
                if not screen.get('url'):
                    raise InvalidConfigurationFileException()
                if not screen.get('format'):
                    raise InvalidConfigurationFileException()
                if (not screen.get('data') or
                        screen['data'] is None):
                    raise InvalidConfigurationFileException()
                if not screen.get('main'):
                    raise InvalidConfigurationFileException()
