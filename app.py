from flask import Flask, render_template, session, redirect, url_for
from controllers.auth_controller import auth_bp
from controllers.catalog_controller import catalog_bp
from controllers.cart_controller import cart_bp
from controllers.admin_controller import admin_bp

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(catalog_bp)
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)