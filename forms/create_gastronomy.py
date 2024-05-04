from flask_wtf import FlaskForm
from wtforms import StringField, FileField


class CreateGastronomy(FlaskForm):
    name = StringField()
    img = FileField()
    text = StringField()

