import unittest
from unittest.mock import MagicMock

from usecases.environment.manager import EnvironmentsManager


class TestEnvironmentManager(unittest.TestCase):
    def test_environment_is_correctly_build_when_there_is_one_screen(self):
        given_configuration = {"environments": [
                {
                    "name": "Test",
                    "screens": [
                        {
                            'name': 'test',
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["version", "commit"],
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        wanted_environment_name = "Test"
        wanted_screen_name = "test"
        wanted_screen_url = "test.fr"
        wanted_screen_format = "json"
        wanted_screen_main_information = "{commit}-{version}"
        environments_manager = EnvironmentsManager("dummy.yml")
        environments_manager.configuration_manager.parse_configuration = MagicMock()
        environments_manager.configuration_manager.get_configuration = MagicMock(return_value=given_configuration)

        result = environments_manager.load_environments()

        first_environment = result[0]
        self.assertEqual(wanted_environment_name, first_environment.get_name())

        first_screen = first_environment.get_screen_list()[0]
        self.assertEqual(wanted_screen_url, first_screen.get_url())
        self.assertEqual(wanted_screen_name, first_screen.get_name())
        self.assertEqual(wanted_screen_format, first_screen.get_format())
        self.assertEqual(wanted_screen_main_information, first_screen.get_main_information())

    def test_environment_is_correctly_build_when_there_is_multiple_environments(self):
        given_configuration = {"environments": [
                {
                    "name": "Test",
                    "screens": [
                        {
                            'name': 'test',
                            'url': 'test.fr',
                            'format': 'json',
                            'data': ["version", "commit"],
                            'main': '{commit}-{version}'
                        }
                    ]
                },
                {
                    "name": "Demo",
                    "screens": [
                        {
                            'name': 'testdemo',
                            'url': 'demo.env.fr',
                            'format': 'json',
                            'data': ["version", "commit"],
                            'main': '{commit}-{version}'
                        }
                    ]
                }
            ]
        }
        wanted_environment_0_name = "Test"
        wanted_environment_0_screen_0_url = "test.fr"
        wanted_environment_0_screen_0_format = "json"
        wanted_environment_1_name = "Demo"

        wanted_environment_1_screen_0_url = "demo.env.fr"
        wanted_environment_1_screen_0_format = "json"
        environments_manager = EnvironmentsManager("dummy.yml")
        environments_manager.configuration_manager.parse_configuration = MagicMock()
        environments_manager.configuration_manager.get_configuration = MagicMock(return_value=given_configuration)

        result = environments_manager.load_environments()

        first_environment = result[0]
        second_environment = result[1]

        self.assertEqual(wanted_environment_0_name, first_environment.get_name())
        first_screen = first_environment.get_screen_list()[0]
        self.assertEqual(wanted_environment_0_screen_0_url, first_screen.get_url())
        self.assertEqual(wanted_environment_0_screen_0_format, first_screen.get_format())

        self.assertEqual(wanted_environment_1_name, second_environment.get_name())
        first_screen = second_environment.get_screen_list()[0]
        self.assertEqual(wanted_environment_1_screen_0_url, first_screen.get_url())
        self.assertEqual(wanted_environment_1_screen_0_format, first_screen.get_format())
