import yaml

from datasources.configuration.exceptions \
    import UnknownConfigurationFileTypeException


class ConfigurationReader():
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        if (self.file_name.endswith(".yml") or
                self.file_name.endswith(".yaml")):
            return self.read_yaml_configuration()
        else:
            raise UnknownConfigurationFileTypeException()

    def read_yaml_configuration(self):
        with open(self.file_name, 'r') as stream:
            data = yaml.safe_load(stream)
        return data
