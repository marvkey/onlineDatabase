from sqlalchemy.sql.expression import false
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(150),unique=True)

    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    username = db.Column(db.String(150))

    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    file =db.relationship("SavedItem",backref="user",passive_deletes=True)

class SavedItem(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    file = db.Column(db.LargeBinary)
    name = db.Column(db.String(150),nullable=False)
    Description = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)