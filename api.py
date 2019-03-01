from flask import Blueprint

route_api = Blueprint("api", __name__)


@route_api.route("/")
def index():
    return "api index page"


@route_api.route("/hello")
def hello_world():
    return "api hello world"
