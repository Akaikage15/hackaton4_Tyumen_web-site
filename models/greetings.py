from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db


class Greetings(db.Model):
    __tablename__ = 'greetings'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50))
    text = db.Column(String(1000))