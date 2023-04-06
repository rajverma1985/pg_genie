import os
from urllib.parse import quote_plus
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config

db = SQLAlchemy()
login = LoginManager()
password = quote_plus(f"{os.environ['DB_PASSWORD']}")
DB_URI = f"postgresql://{os.environ['DB_USER']}:{password}@{os.environ['DB_SERVER']}/{os.environ['DB']}"


# login.login_message = _l('Please log in to access this page.')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_extensions(app)
    register_bp(app)
    return app


def register_bp(app):
    # get blueprints and register them
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # get all the views
    from app.errors import handlers
    from app.main import views
    from app.api import views
    from app.auth import views


def register_logger():
    pass


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app)
    login.login_view = 'auth.login'
    login.init_app(app)
    mail = Mail()
    mail.init_app(app)
    bootstrap = Bootstrap()
    bootstrap.init_app(app)
    moment = Moment()
    moment.init_app(app)
