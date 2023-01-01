from flask import Blueprint, render_template , request, redirect, url_for, flash
from models.ModelUsuarios import Users
from utils.conexion import db
from flask_login import login_user, logout_user#, login_required

login = Blueprint('login', __name__)

@login.route('/')
@login.route('/index')
def index():
    return render_template('login.html')

@login.route('/logear', methods=['GET','POST'])
def logear():
    user = Users
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        user = Users.query.filter_by(nickname=nickname).first()
        if user is not None and user.check_pw(password):
            login_user(user)
            print('usuario')
            return redirect(url_for('operations.welcomeUser'))
        else:
            flash('Usuario o password no valido!')
            return redirect(url_for('login.index'))
    else:
        return redirect(url_for('login.index'))

@login.route('/register')
def register():
    return render_template('register_user.html')

@login.route('/logout')
def salir():
    logout_user()
    return redirect(url_for('login.index'))