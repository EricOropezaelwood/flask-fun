from flask import Flask, render_template, current_app, request, Response
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Index():


class ExampleClass():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        #self.app.config['SECRET_KEY'] = "supersecretkey"

        self.first_input = None
        self.second_input = None

    def index(self):
        return render_template("index.html")

    def query(self):
        title = "Query stuff"
        return render_template("query.html", title=title)

    def form(self):
        title = "Query stuff"

        input_one = 'time'
        input_two = 'location'

        server.first_input = request.form.get(input_one)
        server.second_input = request.form.get(input_two)

        return render_template("form.html", title=title,
                               first_input=server.first_input,
                               second_input=server.second_input)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None,
                     methods=None):

        self.app.add_url_rule(endpoint, endpoint_name,
                              handler, methods)

    def run(self):
        self.app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=False)

    def start(self):

        # add endopints

        self.add_endpoint(endpoint='/', endpoint_name='index',
                          handler=self.index)
        self.add_endpoint(endpoint='/query', endpoint_name='query',
                          handler=self.query)
        self.add_endpoint(endpoint='/form', endpoint_name='form',
                          handler=self.form, methods=["POST"])

        # start the flask app
        self.run()


# @server.app.route('/')
# def index():
#     return render_template("index.html")

# # @server.app.route('/about')
# # def about():
# #     names = ["Eric", "Other", "Random"]
# #     return render_template("about.html", names=names)
#
# @server.app.route('/query')
# def query():
#     title = "querystuff"
#     return render_template("query.html", title=title)
#
# @server.app.route('/form', methods=["POST"])
# def form():
#     title = "Newsletter stuff"
#
#     server.first_input = request.form.get("time")
#     server.second_input = request.form.get("location")
#     return render_template("form.html", title=title, first_input=server.first_input,
#                            second_input=server.second_input)

if __name__ == "__main__":
    server = ExampleClass()
    server.start()

