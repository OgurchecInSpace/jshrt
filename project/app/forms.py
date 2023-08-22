from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from app.models import UrlData


# Форма для отправки. В данный момент не нужна, так как была заменена обычным JS
class MainForm(FlaskForm):
    url = StringField('Url', validators=[DataRequired()])
    button = SubmitField('Get short url')
