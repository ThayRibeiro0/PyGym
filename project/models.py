from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # user = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fullname = db.Column(db.String(150))

class Student(db.Model, UserMixin):
    # student = "student"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150))
    birthdate = db.Column(db.Integer)
    address = db.Column(db.String(150))
    cellphone = db.Column(db.Integer)
    course = db.Column(db.String(150))
    payment = db.Column(db.String(150))