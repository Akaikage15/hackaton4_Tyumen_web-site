from flask_wtf import FlaskForm
from wtforms import StringField, DateField


class CreateQuests(FlaskForm):
    name = StringField()
    date = DateField()
    text = StringField()