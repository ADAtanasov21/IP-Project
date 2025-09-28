from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.catalog_service import get_all_products, search_products

catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/catalog')
def catalog():
    # Проверка дали потребителят е влязъл
    if 'user_id' not in session:
        flash('Моля, влезте в профила си за да разгледате каталога!', 'error')
        return redirect(url_for('auth.login'))

    search_term = request.args.get('search', '')
    color_filter = request.args.get('color', '')
    size_filter = request.args.get('size', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    if search_term or color_filter or size_filter or min_price or max_price:
        products = search_products(search_term, color_filter, size_filter, min_price, max_price)
    else:
        products = get_all_products()

    return render_template('catalog.html', products=products)