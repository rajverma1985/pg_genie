from flask_login import UserMixin
from app import db


class LoginData(UserMixin, db.Model):
    __tablename__ = "login_data"
    id = db.Column(db.Integer(20), primary_key=True, nullable=False)
    login = db.Column(db.String(20), 'login', nullable=False)
    login_time = db.Column(db.DateTime, 'login', nullable=False)
    logout_time = db.Column(db.DateTime, 'logout', nullable=False)


class Registration(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(100))


class GenerateReports(db.Model):
    __tablename__ = "Reports"
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(250), nullable=False)
    generate_by = db.Column(db.String(250), unique=True, nullable=False)
