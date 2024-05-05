from flask_wtf import FlaskForm
from wtforms import StringField, FileField


class CreateGreetings(FlaskForm):
    name = StringField()
    text = StringField()