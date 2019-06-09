from usecases.screen.databuilder import ScreenDataBuilder


class EnvironmentDataBuilder():
    def build_environment(self, environment):
        build = {
            "name": environment["name"]
        }
        screen_builder = ScreenDataBuilder()
        screen_list = []

        for screen in environment.get_screen_list:
            screen_list.append(screen_builder.build_data(screen))

        build["screens"] = screen_list
        return build
