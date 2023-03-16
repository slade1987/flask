from flask import Flask
from blog.user.views import user
from blog.report.views import report
from blog.hw.views import hw

# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "Hello!"
#
#
# @app.route("/greet/<name>/")
# def greet_name(name: str):
#     return f"Hello {name}!"

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(hw)
