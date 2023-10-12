from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("Sign Up")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    passwordConfirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password does not match")])
    submit = SubmitField("Sign Up")

class EditProfile(FlaskForm):
    pass

class CreatePost(FlaskForm):
    pass

class EditPost(FlaskForm):
    pass