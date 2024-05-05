from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(200))
    quests_id = db.Column(db.Integer, ForeignKey('quests.id'))
    quests = relationship('Quests', backref='users')

    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False