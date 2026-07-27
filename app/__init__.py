from flask import Flask

def Create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        return "Welcome to AI Blog"

    return app

