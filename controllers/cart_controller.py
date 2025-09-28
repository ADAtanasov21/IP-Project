from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.cart_service import CartService
from services.catalog_service import CatalogService

cart_bp = Blueprint('cart', __name__)
cart_service = CartService()
catalog_service = CatalogService()


@cart_bp.route('/add/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('Трябва да сте влезли в профила си!')
        return redirect(url_for('auth.login'))

    size = request.args.get('size')
    if not size:
        flash('Моля изберете размер!')
        return redirect(url_for('catalog.catalog'))

    cart_service.add_to_cart(session['user_id'], product_id, size)
    flash('Продуктът е добавен в кошницата!')
    return redirect(url_for('catalog.catalog'))


@cart_bp.route('/view')
def view_cart():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    cart_items = cart_service.get_cart_items(session['user_id'])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)


@cart_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        address = request.form['address']
        payment = request.form['payment']

        if cart_service.process_order(session['user_id'], address, payment):
            flash('Поръчката е обработена успешно!')
            return redirect(url_for('catalog.catalog'))
        else:
            flash('Някои продукти няма в наличност!')

    cart_items = cart_service.get_cart_items(session['user_id'])
    total = sum(item['price'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)