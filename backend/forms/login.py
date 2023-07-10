from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('Submit')