from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if auth_service.register_user(email, password):
            print(f"Потвърждение за регистрация изпратено на {email}")
            flash('Регистрацията беше успешна!')
            return redirect(url_for('auth.login'))
        else:
            flash('Потребител с този имейл вече съществува!')

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = auth_service.login_user(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            session['is_admin'] = user.get('is_admin', False)
            return redirect(url_for('catalog.catalog'))
        else:
            flash('Невалиден имейл или парола!')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))