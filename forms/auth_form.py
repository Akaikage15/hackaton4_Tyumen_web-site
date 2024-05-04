from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class AuthForm(FlaskForm):
    username = StringField(label="Имя Пользователя")
    password = PasswordField(label="Пароль")
