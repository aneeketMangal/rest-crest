from restcrest.forms.imports import *

class LoginForm(FlaskForm):
    username = StringField('usermame', validators = [DataRequired(), Length(min = 2, max = 20)])
    password = PasswordField('password', validators = [DataRequired()])
    remember = BooleanField('remember')
    submit = SubmitField('login')