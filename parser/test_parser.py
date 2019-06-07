import unittest
from unittest.mock import MagicMock

from parser.configuration import Configuration
from parser.exceptions import InvalidConfigurationFileException


class TestParser(unittest.TestCase):

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
        configuration_parser = Configuration()
        configuration_parser.get_file_content = MagicMock(return_value=wanted)

        result = configuration_parser.parse("dummy.yml")

        self.assertEqual(wanted, result)

    def test_if_parser_throw_an_exception_when_file_is_invalid(self):
        wanted = {'nothing': 'nothing'}
        configuration_parser = Configuration()
        configuration_parser.get_file_content = MagicMock(return_value=wanted)

        try:
            configuration_parser.parse("dummy.yml")

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
        configuration_parser = Configuration()
        configuration_parser.get_file_content = MagicMock(return_value=wanted)

        result = configuration_parser.parse("dummy.yml")

        self.assertEqual(wanted, result)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
