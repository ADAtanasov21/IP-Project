class BaseService:

    def __init__(self):
        self.data = []
        self.next_id = 1

    def get_all(self):
        return self.data

    def get_by_id(self, item_id):
        return next((item for item in self.data if item['id'] == item_id), None)


class OrderService(BaseService):
    def __init__(self):
        super().__init__()
        self.data = []
        self.next_id = 1

    def get_user_orders(self, user_id):
        return [order for order in self.data if order['user_id'] == user_id]

    def create_order(self, user_id, items, address, payment):
        order = {
            'id': self.next_id,
            'user_id': user_id,
            'items': items,
            'address': address,
            'payment': payment,
            'total': sum(item['price'] for item in items)
        }
        self.data.append(order)
        self.next_id += 1
        return order