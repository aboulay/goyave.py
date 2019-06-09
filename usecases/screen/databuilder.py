import requests

from usecases.screen.exceptions import UnknownResponseFormat

STATUS_OK = "OK"
STATUS_FAILED = "KO"
INFORMATION_MISSING = "N/A"


class ScreenDataBuilder():
    def build_data(self, screen):
        response = self.call_endpoint(screen.get_url(), screen.get_format())
        if response["status_code"] != 200:
            build = self.build_error_answer(screen, response["body"])
        else:
            build = self.build_ok_answer(screen, response["body"])
        return build

    def call_endpoint(self, url, format):
        response = requests.get(url)
        if format != "json":
            raise UnknownResponseFormat()
        return {
            "status_code": response.status_code,
            "body": response.json()
        }

    def build_error_answer(self, screen, response_body):
        build = {
            "name": screen.get_name(),
            "url": screen.get_url(),
            "status": STATUS_FAILED,
            "data": [],
            "main_information": INFORMATION_MISSING
        }
        return build

    def build_ok_answer(self, screen, response_body):
        processed_data = self.__handle_data(screen, response_body)
        build = {
            "name": screen.get_name(),
            "url": screen.get_url(),
            "status": STATUS_OK,
            "data": processed_data,
            "main_information": self.__build_main_information(screen,
                                                              processed_data)
        }
        return build

    def __handle_data(self, screen, response_body):
        screen_datas = screen.get_data()
        post_treatment_datas = {}
        for data in screen_datas:
            if not response_body.get(data):
                post_treatment_datas[data] = INFORMATION_MISSING
            else:
                post_treatment_datas[data] = response_body.get(data)
        return post_treatment_datas

    def __build_main_information(self, screen, processed_datas):
        main_information = screen.get_main_information()
        for key, value in processed_datas.items():
            main_information = main_information.replace("{" + key + "}", value)
        return main_information
