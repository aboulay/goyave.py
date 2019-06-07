import unittest

from usecases.orchestrator.orchestrator import Orchestrator


class TestOrchestrator(unittest.TestCase):
    def test_api_managers_list_initialization_with_one_element(self):
        given_configuration = {'targets': [
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
        wanted = [{'name': 'Demo environment', 'url': 'test.fr'}]
        orchestrator = Orchestrator("dummy.yml")
        orchestrator.configuration_manager.configuration = given_configuration
        orchestrator.update_api_manager_list()

        result = orchestrator.get_api_manager_list()

        for i in range(len(result)):
            self.assertEqual(wanted[i],
                             result[i].dump(),
                             "Current index: " + str(i))
    
    def test_api_managers_list_initialization_with_two_elements(self):
        given_configuration = {'targets': [
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
                'name': 'Test2 environment',
                'url': 'test2.fr',
                'format': 'json',
                'wanted_field': [
                    {'version': 'version'},
                    {'commit': 'commit'}
                   ],
                'main_output': '{commit}-{version}'
            }
        ]}
        wanted = [{'name': 'Demo environment', 'url': 'test.fr'},
                  {'name': 'Test2 environment', 'url': 'test2.fr'}]
        orchestrator = Orchestrator("dummy.yml")
        orchestrator.configuration_manager.configuration = given_configuration
        orchestrator.update_api_manager_list()

        result = orchestrator.get_api_manager_list()

        for i in range(len(result)):
            self.assertEqual(wanted[i],
                             result[i].dump(),
                             "Current index: " + str(i))
