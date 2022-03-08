from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now() )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    maxes = db.relationship('Maxes')
  

class Maxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    benchmax = db.Column(db.String(1000))
    deadmax = db.Column(db.String(1000))
    squatmax = db.Column(db.String(1000))
    pdeadmax = db.Column(db.String(1000))
    psquatmax = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

        