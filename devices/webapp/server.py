from flask import Flask, render_template

from controllers.environment import EnvironmentController

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


class WebServer():
    def __init__(self, configuration_file, refresh_time=10):
        controller = EnvironmentController(configuration_file)
        self.environments = controller.get_data()
        self.refresh_time = refresh_time

    def run(self):
        app.run(debug=True, host='0.0.0.0')
