from flask import Flask, render_template, current_app, request, \
    Response
from flask_restful import Api, Resource, reqparse
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Index(Resource):
    def get(self):
        return Response(render_template("index.html"), mimetype='text/html')

class Query(Resource):
    def get(self):
        title = "Query stuff"
        return Response(render_template("query.html", title=title), mimetype='text/html')

class Form(Resource):
    def __init__(self):
        self.input_data = reqparse.RequestParser()
        self.input_data.add_argument("time", type=str)
        self.input_data.add_argument("location", type=str)

    def post(self):
        args = self.input_data.parse_args()
        print(args)
        return "OK"

    def get(self):
        title = "Query stuff"

        input_one = 'time'
        input_two = 'location'

        server.first_input = request.form.get(input_one)
        server.second_input = request.form.get(input_two)

        return Response(render_template("form.html", title=title,
                               first_input=server.first_input,
                               second_input=server.second_input), mimetype='text/html')

class ExampleClass():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        # self.app.config['SECRET_KEY'] = "supersecretkey"

        self.first_input = None
        self.second_input = None

    def add_all_resources(self):
        self.api.add_resource(Index, '/')
        self.api.add_resource(Query, '/query')
        self.api.add_resource(Form, '/form')

    def run(self):
        self.app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=False)

    def start(self):
        self.add_all_resources()
        # start the flask app
        self.run()


if __name__ == "__main__":
    server = ExampleClass()
    server.start()


############################################################
# class InputFormData(Resource):
# def __init__(self, controller):
# self.controller = controller
# self.input_data = reqparse.RequestParser()
# self.input_data.add_argument("first_input",type=str)
# self.input_data.add_argument("second_input",type=str)
#
# def post(self):
# args = self.input_data.parse_args()
# print(args)
# return "OK"
#
# class WorkflowRequestInjectorController:
# def __init__(self, server):
# self.app = Flask(__name__)
# self.api = Api(app)
#
# def startup(self):
#
# self.api.add_resource(
# InputFormData,
# '/forms',
# resource_class_args=[self])