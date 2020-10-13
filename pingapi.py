from flask import Flask

application = Flask(__name__)


@application.route("/ping")
def ping():
    return ("", 200)
