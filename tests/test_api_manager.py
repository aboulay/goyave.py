import unittest

from usecases.api.manager import ApiManager


class TestApiManager(unittest.TestCase):
    def test_if_print_content_if_str_or_repr_is_called(self):
        name = "Demo Environment"
        url = "test.fr"
        wanted = {"name": name, "url": url}

        api_manager = ApiManager(name, url)
        result = api_manager.dump()

        self.assertEqual(wanted, result)
