from datasources.configuration.file_reader import ConfigurationReader
from usecases.configuration.data_validation import DataChecker


class ConfigurationManager():
    def __init__(self, configuration_file):
        self.configuration_reader = ConfigurationReader(configuration_file)

    def parse_configuration(self):
        configuration = self.configuration_reader.read()
        DataChecker.check_content_is_valid(configuration)
        self.configuration = configuration

    def get_configuration(self):
        return self.configuration
