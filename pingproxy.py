import requests
from flask import Flask

from settings import pingapi_url

application = Flask(__name__)


@application.route("/ping")
def ping():
    try:
        r = requests.get(pingapi_url)
        r.raise_for_status()
    except Exception as e:
        print(e)
        return ("", 500)
    else:
        return ("", 200)
