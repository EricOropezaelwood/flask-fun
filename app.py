from flask import Flask, render_template, current_app, request
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ExampleClass():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.app.config['SECRET_KEY'] = "supersecretkey"

        self.first_input = None
        self.second_input = None

    def start(self):
        self.app.run(host='0.0.0.0', port=3000, debug=True)

server = ExampleClass()


@server.app.route('/')
def index():
    return render_template("index.html")

@server.app.route('/about')
def about():
    names = ["Eric", "Other", "Random"]
    return render_template("about.html", names=names)

@server.app.route('/subscribe')
def subscribe():
    title = "Newsletter stuff"
    return render_template("subscribe.html", title=title)

@server.app.route('/form', methods=["POST"])
def form():
    title = "Newsletter stuff"

    server.first_input = request.form.get("time")
    server.second_input = request.form.get("location")
    return render_template("form.html", title=title, first_input=server.first_input,
                           second_input=server.second_input)

if __name__ == "__main__":
    server.start()

