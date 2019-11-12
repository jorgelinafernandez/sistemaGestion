from wtforms import Form, TextField, BooleanField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(Form):
    username = TextField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])


class RegisterForm(Form):
    username = TextField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    repassword = PasswordField('repassword', validators=[InputRequired()])
