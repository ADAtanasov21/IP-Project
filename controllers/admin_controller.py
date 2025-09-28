from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.catalog_service import get_all_products, add_product, update_product, delete_product, get_product_by_id

admin_bp = Blueprint('admin', __name__)


def admin_required():
    return session.get('is_admin', False)


@admin_bp.route('/admin')
def admin_panel():
    if not admin_required():
        flash('Admin access required!', 'error')
        return redirect(url_for('auth.login'))

    products = get_all_products()
    return render_template('admin.html', products=products)


@admin_bp.route('/admin/add_product', methods=['GET', 'POST'])
def add_product_route():
    if not admin_required():
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        color = request.form['color']
        sizes = request.form['sizes'].split(',')
        price = float(request.form['price'])
        stock = int(request.form['stock'])

        add_product(name, description, color, sizes, price, stock)
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.admin_panel'))

    return render_template('add_product.html')


@admin_bp.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if not admin_required():
        return redirect(url_for('auth.login'))

    product = get_product_by_id(product_id)
    if not product:
        flash('Product not found!', 'error')
        return redirect(url_for('admin.admin_panel'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        color = request.form['color']
        sizes = request.form['sizes'].split(',')
        price = float(request.form['price'])
        stock = int(request.form['stock'])

        update_product(product_id, name, description, color, sizes, price, stock)
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin.admin_panel'))

    return render_template('edit_product.html', product=product)


@admin_bp.route('/admin/delete_product/<int:product_id>')
def delete_product_route(product_id):
    if not admin_required():
        return redirect(url_for('auth.login'))

    delete_product(product_id)
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin.admin_panel'))