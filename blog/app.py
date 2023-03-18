from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.hw.views import hw
from blog.report.views import report
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '111222333'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlit4e:///db.sqlite'

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(hw)
