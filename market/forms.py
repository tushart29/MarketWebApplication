from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

# will inherit from FlaskForm class I imported
class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        # asking entire users object if there is a user with the username to check from the registration form
        user = User.query.filter_by(username = username_to_check.data).first()
        # bascially verifying the user is in the database
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    # [] is there to verify informaiton
    username = StringField(label='User Name:', validators=[Length(min=2, max= 30), DataRequired()])

    # checks if value is an email address
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    # PasswordField checks if both passwords are equal
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    # verifys if password1 and password2 is confirmed
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label = 'User Name' ,validators=[DataRequired()])
    password = PasswordField(label = 'Password',validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")



