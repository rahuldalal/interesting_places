from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your first name')],
                             render_kw={'placeholder':'Please enter your first name'})
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your last name')],
                            render_kw={'placeholder': 'Please enter your last name'})
    email = StringField('Email',
                        validators=[DataRequired('Please enter your email'), Email('Please enter proper email')],
                        render_kw={'placeholder': 'Please enter your email'})
    pwd = PasswordField('Password', validators=[DataRequired('Please enter your password'), Length(min=6,
                                                                                                   message='The password should consist of at least 6 characters')],
                        render_kw={'placeholder': 'Password should be minimum 6 characters'})
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Please enter your email for logging in'),
                                             Email('Please enter a valid email')],
                        render_kw={'placeholder': 'abc@xyz.com'})
    pwd = PasswordField('Password', validators=[DataRequired('Please enter your password for logging in'),
                                                Length(min=6, message='Please enter correct password')],
                        render_kw={'placeholder': 'Enter your password...'})
    submit = SubmitField('Sign In')
