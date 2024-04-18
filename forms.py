from flask_wtf import FlaskForm  # Import FlaskForm from flask_wtf module
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # Import form field types from wtforms module
from wtforms.validators import DataRequired, Length, Email, EqualTo  # Import validators from wtforms module


class RegistrationForm(FlaskForm):
    # Define form fields for user registration
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  # Username field with validators
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email field with validators
    password = PasswordField('Password', validators=[DataRequired()])  # Password field with validators
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  # Confirm password field with validators
    submit = SubmitField('Sign Up')  # Submit button for form


class LoginForm(FlaskForm):
    # Define form fields for user login
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email field with validators
    password = PasswordField('Password', validators=[DataRequired()])  # Password field with validators
    remember = BooleanField('Remember Me')  # Checkbox for remember me option
    submit = SubmitField('Login')  # Submit button for form
