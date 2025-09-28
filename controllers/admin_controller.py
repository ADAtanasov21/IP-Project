from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.catalog_service import CatalogService

admin_bp = Blueprint('admin', __name__)
catalog_service = CatalogService()


def admin_required():
    if 'user_id' not in session or not session.get('is_admin'):
        return redirect(url_for('auth.login'))
    return None


@admin_bp.route('/')
def admin_panel():
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    products = catalog_service.get_products()
    return render_template('admin_panel.html', products=products)


@admin_bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'color': request.form['color'],
            'sizes': request.form['sizes'].split(','),
            'price': float(request.form['price']),
            'quantity': int(request.form['quantity']),
            'image': request.form['image']
        }

        catalog_service.add_product(product_data)
        flash('Продуктът е добавен успешно!')
        return redirect(url_for('admin.admin_panel'))

    return render_template('admin_add_product.html')


@admin_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'color': request.form['color'],
            'sizes': request.form['sizes'].split(','),
            'price': float(request.form['price']),
            'quantity': int(request.form['quantity']),
            'image': request.form['image']
        }

        catalog_service.update_product(product_id, product_data)
        flash('Продуктът е обновен успешно!')
        return redirect(url_for('admin.admin_panel'))

    product = catalog_service.get_product_by_id(product_id)
    return render_template('admin_edit_product.html', product=product)


@admin_bp.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    catalog_service.delete_product(product_id)
    flash('Продуктът е изтрит!')
    return redirect(url_for('admin.admin_panel'))