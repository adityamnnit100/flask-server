from flask import Flask


def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<p> Welcome to Flask Server </p>'
    return app