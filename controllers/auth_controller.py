from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.auth_service import register_user, login_user, logout_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        if register_user(email, password, name):
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Email already exists!', 'error')

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = login_user(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            session['is_admin'] = user.get('is_admin', False)
            flash('Login successful!', 'success')
            return redirect(url_for('catalog.catalog'))
        else:
            flash('Invalid credentials!', 'error')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))