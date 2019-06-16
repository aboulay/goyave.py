from flask import Flask, Response, render_template

from controllers.environment import EnvironmentController
from presenters.environment import EnvironmentPresenter


class EndpointAction(object):

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        answer = self.action()
        self.response = Response(answer, status=200, headers={})
        return self.response


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)

    def run(self):
        self.app.run(debug=True, host='0.0.0.0')

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


class WebServer():
    def __init__(self, configuration_file, refresh_time=10):
        controller = EnvironmentController(configuration_file)
        self.environments = controller.get_data()
        self.presenter = EnvironmentPresenter()
        self.refresh_time = refresh_time
        self.app_server = FlaskAppWrapper(__name__)
        self.app_server.add_endpoint(endpoint="/",
                                     endpoint_name="/",
                                     handler=self.__index)

    def __index(self):
        environments = self.presenter.presents(self.environments)
        return render_template('index.html', environments=environments)

    def run(self):
        self.app_server.run()
