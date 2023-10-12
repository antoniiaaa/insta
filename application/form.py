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
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    # email = StringField('Email', validators=[DataRequired(), Email(), Length(max=128)])
    bio = TextAreaField('Bio', validators=[Length(max=256)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')


class CreatePost(FlaskForm):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Create Post')

class EditPost(FlaskForm):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Edit Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')