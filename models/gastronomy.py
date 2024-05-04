from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db


class Gastronomy(db.Model):
    __tablename__ = 'gastronomy'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50))
    text = db.Column(String(1000))
    img = db.Column(String(100))
