import yaml

from parser.datachecker import data_checker


class Configuration():
    def parse(self, configuration_file):
        content = self.get_file_content(configuration_file)
        data_checker.check_content_is_valid(content)
        return content

    def get_file_content(self, configuration_file):
        with open(configuration_file, 'r') as stream:
            data = yaml.safe_load(stream)
        return data
