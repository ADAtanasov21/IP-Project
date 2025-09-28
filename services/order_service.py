from services.cart_service import get_cart, get_cart_total
from services.catalog_service import reduce_stock

orders = []
order_id_counter = 1


def create_order(user_id, address, payment_method):
    global order_id_counter

    cart_items = get_cart(user_id)
    if not cart_items:
        return False

    for item in cart_items:
        if not reduce_stock(item['product_id'], item['quantity']):
            return False

    order = {
        'id': order_id_counter,
        'user_id': user_id,
        'items': cart_items.copy(),
        'total': get_cart_total(user_id),
        'address': address,
        'payment_method': payment_method,
        'status': 'confirmed'
    }

    orders.append(order)
    order_id_counter += 1

    print(f"Order confirmation sent for Order #{order['id']}")

    return True


def get_user_orders(user_id):
    return [order for order in orders if order['user_id'] == user_id]