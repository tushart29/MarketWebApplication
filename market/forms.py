from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


# will inherit from FlaskForm class I imported
class RegisterForm(FlaskForm):
    username = StringField(label='User Name:')
    email_address = StringField(label='Email Address:')
    # PasswordField checks if both passwords are equal
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')

