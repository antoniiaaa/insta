from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from application.utils import exists_email, not_exists_email, exists_username

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("Sign Up")
# DDDDONNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEE

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8), exists_username])
    fullname = StringField("Full Name", validators=[DataRequired(), Length(min=4, max=16)])
    email = StringField("Email", validators=[DataRequired(), Email(), exists_email])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    passwordConfirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("Sign Up")
    # DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

class EditProfile(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=12), exists_username])
    email = StringField('Email', validators=[DataRequired(), Email(), exists_email])
    # bio = TextAreaField('Bio', validators=[Length(max=256)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Profile')

class ResetPasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("Reset Password")
    # DONEEEEEEEEEEEEEE

class ForgotPasswordForm(FlaskForm):
    email = PasswordField("Email", validators=[DataRequired(), not_exists_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send link verification to Email")
    #DONENEEEEEEEEEEEEEEEE

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm New Password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("Reset Password")
    #DONEEEEEEEE

class CreatePostForm(FlaskForm):
    caption = TextAreaField('Caption')
    image = FileField('Upload Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Create Post')
    #DONEEEEEEEEEEEEEEEEEE

class EditPost(FlaskForm):
    caption = StringField("Caption")
    submit = SubmitField('Save Changes')
    #DONEEEEEEEEEEE