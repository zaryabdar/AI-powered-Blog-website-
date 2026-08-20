from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import file_allowed

class RegistrationForm(FlaskForm):
    username =StringField("Username", validators=[DataRequired(),Length(min=5, max=20)])
    email =StringField("Email", validators=[DataRequired(),Email()])
    password =PasswordField("Password", validators=[DataRequired(),Length(min=8, max=20)])
    confirm_password =PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email =StringField("Email", validators=[DataRequired(),Email()])
    password =PasswordField("Password", validators=[DataRequired(),Length(min=8, max=20)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class EditProfileForm(FlaskForm):
    username = StringField("Usename",validators=[DataRequired(),Length(min=5, max=20)])
    bio = TextAreaField("Bio", validators=[Length(max=500)])
    profile_img = FileField("Profile image", validators=[file_allowed(["jpg","jpeg","png"],"images only!")])
    submit = SubmitField("Save Changes")
                        