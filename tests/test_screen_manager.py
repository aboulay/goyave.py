import unittest
from unittest.mock import MagicMock

from usecases.screen.manager import ScreensManager


class TestScreenManager(unittest.TestCase):
    def test_screen_are_correcly_created_when_configuration_has_one_element(self):
        given_configuration = {'targets': [
            {
                'name': 'Demo environment',
                'url': 'test.fr',
                'format': 'json',
                'data': [
                    {'version': 'version'},
                    {'commit': 'commit'}
                   ],
                'main': '{commit}-{version}'
            }
        ]}
        wanted_name = "Demo environment"
        wanted_url = "test.fr"
        wanted_format = "json"
        wanted_main_information = "{commit}-{version}"
        screen_manager = ScreensManager("dummy.yml")
        screen_manager.configuration_manager.parse_configuration = MagicMock(return_value="")
        screen_manager.configuration_manager.get_configuration = MagicMock(return_value=given_configuration)

        screen_manager.load_screens()

        result = screen_manager.get_screen_list()

        self.assertEqual(wanted_name, result[0].get_name())
        self.assertEqual(wanted_url, result[0].get_url())
        self.assertEqual(wanted_format, result[0].get_format())
        self.assertEqual(wanted_main_information, result[0].get_main_information())
