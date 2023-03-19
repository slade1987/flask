from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

login_manager = LoginManager()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '111222333'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    from blog.auth.views import auth
    from blog.hw.views import hw
    from blog.report.views import report
    from blog.user.views import user

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(hw)
    app.register_blueprint(auth)

