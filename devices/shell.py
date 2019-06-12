import time
import os

from controllers.environment import EnvironmentController
from presenters.environment import EnvironmentPresenter

STATUS_OK = "OK"
STATUS_FAILED = "KO"

COLOR_RED = "\033[1;31m"
COLOR_GREEN = "\033[1;32m"
COLOR_HIGHLIGHT = "\033[1;37m"
COLOR_BASE = "\033[0m"


class Shell():
    def __init__(self, configuration_file, refresh_time=10):
        controller = EnvironmentController(configuration_file)
        self.environments = controller.get_data()
        self.presenter = EnvironmentPresenter()
        self.refresh_time = refresh_time

    def run(self):
        while True:
            self.__clear_screen()
            self._print_settings_data()
            self.__print_ascii()
            environments = self.presenter.presents(self.environments)
            for environment in environments:
                self.__print_environment(environment["name"], environment["screens"])
            time.sleep(self.refresh_time)

    def __clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __print_ascii(self):
        print('  ___   __  _  _  __   _  _  ____     ____  _  _ ')
        print(' / __) /  \( \/ )/ _\ / )( \(  __)   (  _ \( \/ )')
        print('( (_ \(  O ))  //    \\\\ \/ / ) _)  _  ) __/ )  / ')
        print(' \___/ \__/(__/ \_/\_/ \__/ (____)(_)(__)  (__/  ')
        print("")

    def _print_settings_data(self):
        print("Refresh time every " + str(self.refresh_time) + " sec.")

    def __print_environment(self, environment_name, screens):
        print("Environment: " + COLOR_HIGHLIGHT + environment_name + COLOR_BASE)
        for screen in screens:
            self.__print_screen(screen)
        print("")

    def __print_screen(self, screen):
        outline = "name: " + COLOR_HIGHLIGHT + screen["name"] + COLOR_BASE
        outline += " -"
        if screen["status"] == STATUS_OK:
            outline += " status: " + COLOR_GREEN + "online" + COLOR_BASE
            outline += " -"
            outline += " " + screen["main_information"]
        elif screen["status"] == STATUS_FAILED:
            outline += " status: " + COLOR_RED + "offline" + COLOR_BASE
        else:
            outline += "Error: Unknown status"
        print(outline)
