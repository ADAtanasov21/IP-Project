from services.catalog_service import get_product_by_id

carts = {}


def add_to_cart(user_id, product_id, size, quantity=1):
    product = get_product_by_id(product_id)
    if not product or product['stock'] < quantity or size not in product['sizes']:
        return False

    if user_id not in carts:
        carts[user_id] = []

    for item in carts[user_id]:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True

    cart_item = {
        'product_id': product_id,
        'name': product['name'],
        'color': product['color'],
        'size': size,
        'price': product['price'],
        'quantity': quantity
    }

    carts[user_id].append(cart_item)
    return True


def get_cart(user_id):
    return carts.get(user_id, [])


def remove_from_cart(user_id, product_id):
    if user_id in carts:
        carts[user_id] = [item for item in carts[user_id] if item['product_id'] != product_id]


def clear_cart(user_id):
    if user_id in carts:
        carts[user_id] = []


def get_cart_total(user_id):
    cart_items = get_cart(user_id)
    return sum(item['price'] * item['quantity'] for item in cart_items)