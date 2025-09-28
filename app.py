from flask import Flask, render_template, redirect, url_for
from controllers.auth_controller import auth_bp
from controllers.catalog_controller import catalog_bp
from controllers.cart_controller import cart_bp
from controllers.admin_controller import admin_bp

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(admin_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Initialize some test data
    from services.auth_service import create_admin_user
    from services.catalog_service import add_sample_products

    print("=== Initializing Shoe Store Application ===")
    create_admin_user()
    add_sample_products()
    print("=== Sample data loaded ===")
    print("Admin login: admin@shoestore.com / admin123")
    print("=======================================")

    app.run(debug=True, host='0.0.0.0', port=5000)