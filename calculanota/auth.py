from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db


auths = Blueprint('auths', __name__)

@auths.route('/task', methods=['GET','POST'])
def task():
    return render_template('task.html')

@auths.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                return redirect(url_for('views.home'))
        
    return render_template('login.html')

@auths.route('/logout')
def logout():
    #logout_user()
    return redirect(url_for('auths.login'))

@auths.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash("Email tem que ser masior q 5 caracteres", category='error')
        elif len(fName) < 2:
            flash("O nome deve ter mais q 2 caracteres", category='error')
        elif len(password1) < 7:
            flash("Senha muito pequena", category='error')
        elif password1 != password2:
            flash("Senhas n batem")
        else:
            n_user = User(email=email, f_name = fName, password = password1)
            db.session.add(n_user)
            db.session.commit()
            flash("Conta criada cm sucesso!!",category='success')

            return redirect(url_for('view.home'))
            #create account
    return render_template("sign-up.html")