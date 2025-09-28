from flask import Blueprint, render_template, request
from services.catalog_service import CatalogService

catalog_bp = Blueprint('catalog', __name__)
catalog_service = CatalogService()


@catalog_bp.route('/catalog')
def catalog():
    search = request.args.get('search', '')
    color = request.args.get('color', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    size = request.args.get('size', '')

    products = catalog_service.get_products()

    if search:
        products = [p for p in products if search.lower() in p['name'].lower() or search.lower() in p['color'].lower()]

    if color:
        products = [p for p in products if color.lower() in p['color'].lower()]

    if min_price:
        products = [p for p in products if p['price'] >= min_price]

    if max_price:
        products = [p for p in products if p['price'] <= max_price]

    if size:
        products = [p for p in products if size in p['sizes']]

    return render_template('catalog.html', products=products)