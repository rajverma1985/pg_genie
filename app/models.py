from flask_login import UserMixin
from app import db


class LoginData(UserMixin, db.Model):
    __tablename__ = "login_data"
    id = db.Column(db.Integer(20), primary_key=True, nullable=False)
    name = db.Column(db.String(20), 'name', nullable=False)
    login_time = db.Column(db.DateTime, 'login', nullable=False)
    logout_time = db.Column(db.DateTime, 'login', nullable=False)