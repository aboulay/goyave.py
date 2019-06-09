import unittest
from unittest.mock import MagicMock

from usecases.configuration.manager import ConfigurationManager
from usecases.configuration.exceptions \
    import InvalidConfigurationFileException
from usecases.configuration.exceptions \
    import UnknownConfigurationFileTypeException


class TestConfigurationManager(unittest.TestCase):
    def test_parser_when_data_are_correct_it_should_return_data(self):
        wanted = {
            'environments': [
                {
                    'name': 'Demo',
                    'screens': [
                        {
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["commit", "version"],
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.read_configuration = MagicMock(return_value=wanted)
        configuration_manager.parse_configuration()

        result = configuration_manager.get_configuration()

        self.assertEqual(wanted, result)

    def test_parser_when_there_is_more_than_one_endpoint(self):
        wanted = {
            'environments': [
                {
                    'name': 'Demo',
                    'screens': [
                        {
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["commit", "version"],
                            'main': '{commit}-{version}'
                        },
                        {
                            'url': 'test2.fr',
                            'format': 'json',
                            'data': ["commit", "version"],
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.read_configuration = MagicMock(return_value=wanted)
        configuration_manager.parse_configuration()

        result = configuration_manager.get_configuration()

        self.assertEqual(wanted, result)
    
    def test_parser_when_there_is_multiples_environments(self):
        wanted = {
            'environments': [
                {
                    'name': 'Demo',
                    'screens': [
                        {
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["commit", "version"],
                            'main': '{commit}-{version}'
                        }
                    ]
                },
                {
                    'name': 'Production',
                    'screens': [
                        {
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["commit", "version"],
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.read_configuration = MagicMock(return_value=wanted)
        configuration_manager.parse_configuration()

        result = configuration_manager.get_configuration()

        self.assertEqual(wanted, result)

    def test_parser_when_data_are_invalid(self):
        wanted = {
            'environments': [
                {
                    'name': 'Demo',
                    'screens': [
                        {
                            'url': 'test.fr',
                            'format': 'json',
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        configuration_manager = ConfigurationManager("dummy.yml")
        configuration_manager.read_configuration = MagicMock(return_value=wanted)

        try:
            configuration_manager.parse_configuration()

            self.assertTrue(False, "parse_configuration does not throw an exception")
        except InvalidConfigurationFileException:
            self.assertTrue(True)

    def test_parser_when_file_type_is_not_a_yaml(self):
        configuration_manager = ConfigurationManager("dummy.jpeg")

        try:
            configuration_manager.parse_configuration()
            self.assertTrue(False, "parse_configuration does not throw an exception")

        except UnknownConfigurationFileTypeException:
            self.assertTrue(True)
