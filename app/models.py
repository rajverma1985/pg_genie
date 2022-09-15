from flask_login import UserMixin
from app import db


class LoginData(UserMixin, db.Model):
    __tablename__ = "login_data"
    id = db.Column(db.Integer(20), primary_key=True, nullable=False)
    login_name = db.Column(db.String(20), 'login', nullable=False)
