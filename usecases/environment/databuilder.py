from usecases.screen.databuilder import ScreenDataBuilder


class EnvironmentDataBuilder():
    def build(self, environment):
        build = {
            "name": environment.get_name()
        }
        screen_builder = ScreenDataBuilder()
        screen_list = []

        for screen in environment.get_screen_list():
            screen_list.append(screen_builder.build(screen))

        build["screens"] = screen_list
        return build
