from restcrest.forms.imports import *


class RegisterForm(FlaskForm):

    username = StringField('Usermame', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    
    # def validate_username(self, username):
    #     databaseLog = self.__database.checkUserNameAvailability(username.data)
    #     if(databaseLog['isAvailable'] == False):
    #         raise ValidationError(databaseLog['errorLog'])
    # def validate_email(self, email):
    #     databaseLog = self.__database.checkEmailAvailability(email.data)
    #     if(databaseLog['isAvailable'] == False):
    #         raise ValidationError(databaseLog['errorLog'])

