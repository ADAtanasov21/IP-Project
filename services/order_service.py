class OrderService:
    def __init__(self):
        self.orders = []
        self.next_id = 1

    def create_order(self, user_id, items, address, payment):
        order = {
            'id': self.next_id,
            'user_id': user_id,
            'items': items,
            'address': address,
            'payment': payment,
            'total': sum(item['price'] for item in items)
        }
        self.orders.append(order)
        self.next_id += 1
        return order