import csv

from flask import (Flask,
    request, render_template,
    redirect, url_for, Response,
    session
)
from flask_login import (
    login_required, logout_user,
    login_user, LoginManager
)

from loginform import LoginForm, RegisterForm
from users import User
from tools import get_clients

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='Secret_key'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sobre')
@login_required
def sobre():
    return render_template('sobre.html')


@app.route('/clientes')
@login_required
def clientes():
    user_id = session['user_id']
    user = User.get(user_id)
    clients = get_clients()
    return render_template(
        'list_clients.html',
        user=user,
        clients=clients
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and user.password == password:
            login_user(user)
        else:
            return Response('Usuario o password incorrectos.')
        return redirect(url_for('home'))
    else:
        return render_template('login.html', form=form)


@app.route("/registro", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        
        user = User.get_by_username(username)

        if password == repassword:
            if not user:
                user = User.create(username, password)
                if user:
                    login_user(user)
                    return redirect(url_for('home'))
            else:
                return Response('El usuario ya existe.')
        else:
            return Response('La password no coincide.')
    else:
        return render_template('registro.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('cerro_sesion.html')


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404


@app.errorhandler(500)
def internal_server_error(error):
   return render_template('500.html', title = '500'), 500