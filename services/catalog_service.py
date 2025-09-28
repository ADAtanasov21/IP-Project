products = []
product_id_counter = 1


def get_all_products():
    return [p for p in products if p['stock'] > 0]


def get_product_by_id(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None


def add_product(name, description, color, sizes, price, stock):
    global product_id_counter

    product = {
        'id': product_id_counter,
        'name': name,
        'description': description,
        'color': color,
        'sizes': [size.strip() for size in sizes],
        'price': price,
        'stock': stock
    }

    products.append(product)
    product_id_counter += 1


def update_product(product_id, name, description, color, sizes, price, stock):
    for product in products:
        if product['id'] == product_id:
            product.update({
                'name': name,
                'description': description,
                'color': color,
                'sizes': [size.strip() for size in sizes],
                'price': price,
                'stock': stock
            })
            return True
    return False


def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]


def search_products(search_term='', color_filter='', size_filter='', min_price=None, max_price=None):
    filtered_products = []

    for product in products:
        if product['stock'] <= 0:
            continue

        if search_term and search_term.lower() not in product['name'].lower() and search_term.lower() not in product[
            'color'].lower():
            continue

        if color_filter and color_filter.lower() != product['color'].lower():
            continue

        if size_filter and size_filter not in product['sizes']:
            continue

        if min_price is not None and product['price'] < min_price:
            continue
        if max_price is not None and product['price'] > max_price:
            continue

        filtered_products.append(product)

    return filtered_products


def reduce_stock(product_id, quantity=1):
    for product in products:
        if product['id'] == product_id:
            if product['stock'] >= quantity:
                product['stock'] -= quantity
                return True
    return False


def add_sample_products():
    sample_products = [
        {
            'name': 'Nike Air Max',
            'description': 'Comfortable running shoes',
            'color': 'Black',
            'sizes': ['38', '39', '40', '41', '42'],
            'price': 120.0,
            'stock': 10
        },
        {
            'name': 'Adidas Ultraboost',
            'description': 'High-performance athletic shoes',
            'color': 'White',
            'sizes': ['37', '38', '39', '40', '41'],
            'price': 150.0,
            'stock': 8
        },
        {
            'name': 'Converse Chuck Taylor',
            'description': 'Classic canvas sneakers',
            'color': 'Red',
            'sizes': ['36', '37', '38', '39', '40', '41', '42'],
            'price': 65.0,
            'stock': 15
        }
    ]

    for product_data in sample_products:
        if not any(p['name'] == product_data['name'] for p in products):
            add_product(**product_data)