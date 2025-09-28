from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.cart_service import add_to_cart, get_cart, remove_from_cart, clear_cart
from services.order_service import create_order

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/add_to_cart/<int:product_id>')
def add_to_cart_route(product_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart', 'error')
        return redirect(url_for('auth.login'))

    size = request.args.get('size')
    if not size:
        flash('Please select a size', 'error')
        return redirect(url_for('catalog.catalog'))

    if add_to_cart(session['user_id'], product_id, size):
        flash('Product added to cart!', 'success')
    else:
        flash('Product not available or out of stock!', 'error')

    return redirect(url_for('catalog.catalog'))


@cart_bp.route('/cart')
def view_cart():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    cart_items = get_cart(session['user_id'])
    total = sum(item['price'] * item['quantity'] for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, total=total)


@cart_bp.route('/remove_from_cart/<int:product_id>')
def remove_from_cart_route(product_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    remove_from_cart(session['user_id'], product_id)
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    cart_items = get_cart(session['user_id'])
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('catalog.catalog'))

    if request.method == 'POST':
        address = request.form['address']
        payment_method = request.form['payment_method']

        if create_order(session['user_id'], address, payment_method):
            clear_cart(session['user_id'])
            flash('Order placed successfully!', 'success')
            return redirect(url_for('catalog.catalog'))
        else:
            flash('Error placing order!', 'error')

    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)