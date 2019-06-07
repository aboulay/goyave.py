import unittest
from unittest.mock import MagicMock

from usecases.configuration.manager import ConfigurationManager
from usecases.configuration.exceptions \
    import InvalidConfigurationFileException


class TestConfigManager(unittest.TestCase):

    def test_if_parser_return_correct_data_when_there_is_no_problem(self):
        wanted = {'targets': [
            {
                'name': 'Demo environment',
                'url': 'test.fr',
                'format': 'json',
                'wanted_field': [
                    {'version': 'version'},
                    {'commit': 'commit'}
                   ],
                'main_output': '{commit}-{version}'
            }
        ]}
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.configuration_reader.read = MagicMock(return_value=wanted)
        configuration_manager.parse_configuration()

        result = configuration_manager.get_configuration()

        self.assertEqual(wanted, result)

    def test_if_parser_throw_an_exception_when_file_is_invalid(self):
        wanted = {'nothing': 'nothing'}
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.configuration_reader.read = MagicMock(return_value=wanted)

        try:
            configuration_manager.parse_configuration()
        except InvalidConfigurationFileException:
            self.assertTrue(True)

    def test_if_parser_return_correct_data_two_env_when_there_no_problem(self):
        wanted = {'targets': [
            {
                'name': 'Demo environment',
                'url': 'test.fr',
                'format': 'json',
                'wanted_field': [
                    {'version': 'version'},
                    {'commit': 'commit'}
                   ],
                'main_output': '{commit}-{version}'
            },
            {
                'name': 'Demo2 environment',
                'url': 'test.fr',
                'format': 'json',
                'wanted_field': [
                    {'version': 'version'},
                    {'commit': 'commit'}
                   ],
                'main_output': '{commit}-{version}'
            }
        ]}
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.configuration_reader.read = MagicMock(return_value=wanted)
        configuration_manager.parse_configuration()

        result = configuration_manager.get_configuration()

        self.assertEqual(wanted, result)
