import unittest
from unittest.mock import MagicMock

from entities.screen import Screen
from usecases.screen.databuilder import ScreenDataBuilder


class TestScreenDataBuilder(unittest.TestCase):
    def test_build_data_when_screen_is_correct(self):
        wanted = {
            "url": "test.fr",
            "status": "OK",
            "data": {'commit': '4f55721f0bb', 'version': '1.4.7'},
            "main_information": "1.4.7-4f55721f0bb"
        }

        given_endpoint_return = {
            "status_code": 200,
            "body": {
                "version": "1.4.7",
                "commit": "4f55721f0bb",
                "test_data": "lifeisshort"
            }
        }

        given_screen = Screen()
        given_screen.set_url("test.fr")
        given_screen.set_format("json")
        given_screen.set_data(["commit", "version"])
        given_screen.set_main_information("{version}-{commit}")

        screen_databuilder = ScreenDataBuilder()
        screen_databuilder.call_endpoint = MagicMock(return_value=given_endpoint_return)

        result = screen_databuilder.build(given_screen)

        self.assertEqual(wanted, result)

    def test_build_data_when_answer_is_incorrect(self):
        wanted = {
            "url": "nowhere.fr",
            "status": "KO",
            "data": {},
            "main_information": "N/A"
        }

        given_endpoint_return = {
            "status_code": 404,
            "body": {}
        }

        given_screen = Screen()
        given_screen.set_url("nowhere.fr")
        given_screen.set_format("json")
        given_screen.set_data(["commit", "version"])
        given_screen.set_main_information("{version}-{commit}")

        screen_databuilder = ScreenDataBuilder()
        screen_databuilder.call_endpoint = MagicMock(return_value=given_endpoint_return)

        result = screen_databuilder.build(given_screen)

        self.assertEqual(wanted, result)
