from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, PasswordField, \
    SelectField, DateField, SelectMultipleField
from choice_options import languages
from controls import get_interests, get_cities


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=12), 
        validators.InputRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=50), 
        validators.InputRequired(), validators.EqualTo('confirm', 
        message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email Address', [validators.Length(min=6, max=35), 
        validators.InputRequired(), validators.Email()])
    name = StringField('Name', [validators.Length(min=2, max=25), 
        validators.InputRequired()])
    surname = StringField('Last name', [validators.Length(min=2, max=35), 
        validators.InputRequired()])
    current_location = StringField('Home city', 
        [validators.Length(min=4, max=35), validators.InputRequired()])
    nationality = StringField('Nationality', 
        [validators.Length(min=4, max=25), validators.InputRequired()])
    date_of_birth = DateField('Your Birthday', [validators.InputRequired()])
    is_buddy = BooleanField('Do you want to be a buddy?')
    is_student = BooleanField('Are you a student?')
    current_uni = StringField('Enter your current University/Facility', 
        [validators.Length(min=4, max=35), validators.InputRequired()])
    mother_tongue = SelectField('Mother tongue', [validators.InputRequired()], 
        choices=languages)
    chosen_interests = SelectMultipleField('Choose your interests', 
        [validators.InputRequired()], choices=get_interests)

class SearchForm(FlaskForm):
    chosen_interest = SelectField('Choose an interest', [validators.InputRequired()], 
        choices=get_interests)
    chosen_city = SelectField('Choose a city to look buddies from', 
        [validators.InputRequired()], choices=get_cities)

class ModifyInfo(FlaskForm):
    chosen_interests = SelectMultipleField('Choose your interests',
        choices=get_interests)
    is_buddy = BooleanField('Do you want to be a buddy?')
    is_student = BooleanField('Are you a student?')
    current_uni = StringField('Enter your current University/Facility', 
        [validators.Length(min=4, max=35)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), 
        validators.Email()])