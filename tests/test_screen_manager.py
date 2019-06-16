import unittest

from usecases.screen.manager import ScreensManager


class TestScreenManager(unittest.TestCase):
    def test_screen_are_correcly_created_when_there_is_one_screen(self):
        given_screens = [
            {
                'name': 'test',
                'url': 'test.fr',
                'format': 'json',
                'data': ["version", "commit"],
                'main': '{commit}-{version}'
            }
        ]

        wanted_name = "test"
        wanted_url = "test.fr"
        wanted_format = "json"
        wanted_main_information = "{commit}-{version}"
        screen_manager = ScreensManager()

        screen_manager.load_screens(given_screens)

        result = screen_manager.get_screen_list()

        screen_0 = result[0]
        self.assertEqual(wanted_name, screen_0.get_name())
        self.assertEqual(wanted_url, screen_0.get_url())
        self.assertEqual(wanted_format, screen_0.get_format())
        self.assertEqual(wanted_main_information, screen_0.get_main_information())

    def test_screen_are_correcly_created_when_there_is_multiple_screens(self):
        given_screens = [
            {
                'name': 'test',
                'url': 'test.fr',
                'format': 'json',
                'data': ["version", "commit"],
                'main': '{commit}-{version}'
            },
            {
                'name': 'test1',
                'url': 'test1.fr',
                'format': 'json',
                'data': ["version", "commit"],
                'main': '{commit}-{version}'
            }
        ]

        wanted_screen_0_name = "test"
        wanted_screen_0_url = "test.fr"
        wanted_screen_0_format = "json"
        wanted_screen_0_main_information = "{commit}-{version}"
        wanted_screen_1_name = "test1"
        wanted_screen_1_url = "test1.fr"
        wanted_screen_1_format = "json"
        wanted_screen_1_main_information = "{commit}-{version}"
        screen_manager = ScreensManager()

        screen_manager.load_screens(given_screens)

        result = screen_manager.get_screen_list()

        screen_0 = result[0]
        self.assertEqual(wanted_screen_0_name, screen_0.get_name())
        self.assertEqual(wanted_screen_0_url, screen_0.get_url())
        self.assertEqual(wanted_screen_0_format, screen_0.get_format())
        self.assertEqual(wanted_screen_0_main_information, screen_0.get_main_information())
        screen_1 = result[1]
        self.assertEqual(wanted_screen_1_name, screen_1.get_name())
        self.assertEqual(wanted_screen_1_url, screen_1.get_url())
        self.assertEqual(wanted_screen_1_format, screen_1.get_format())
        self.assertEqual(wanted_screen_1_main_information, screen_1.get_main_information())
