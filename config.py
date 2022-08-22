import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admins@pg_genie.com']
    LANGUAGES = ['en', 'es']


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql:///" + os.path.join(basedir, "pg_genie_dev")
    IMAGE_UPLOADS = os.path.join(basedir, "uploads")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "pg_genie_test")
    IMAGE_UPLOADS = os.path.join(basedir, "uploads")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_DB_URI") or \
                              "sqlite:///" + os.path.join(basedir, "pg_genie_prod")
    IMAGE_UPLOADS = os.environ.get("FLASK_UPLOADS_FOLDER_URL") or \
                    os.path.join(basedir, "uploads")
