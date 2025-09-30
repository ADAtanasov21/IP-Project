from services.catalog_service import CatalogService

class BaseService:

    def __init__(self):
        self.data = []
        self.next_id = 1

    def get_all(self):
        return self.data

    def get_by_id(self, item_id):
        return next((item for item in self.data if item['id'] == item_id), None)


class CartService(BaseService):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.catalog_service = CatalogService()

    def get_by_id(self, user_id):
        return self.data.get(user_id, [])

    def get_all(self):
        return self.data

    def add_to_cart(self, user_id, product_id, size):
        if user_id not in self.data:
            self.data[user_id] = []

        for item in self.data[user_id]:
            if item['product_id'] == product_id and item['size'] == size:
                item['quantity'] += 1
                return

        product = self.catalog_service.get_product_by_id(product_id)
        if product and product['quantity'] > 0:
            cart_item = {
                'product_id': product_id,
                'name': product['name'],
                'price': product['price'],
                'size': size,
                'image': product['image'],
                'quantity': 1
            }
            self.data[user_id].append(cart_item)

    def get_cart_items(self, user_id):
        return self.get_by_id(user_id)

    def process_order(self, user_id, address, payment):
        cart_items = self.get_cart_items(user_id)

        for item in cart_items:
            product = self.catalog_service.get_product_by_id(item['product_id'])
            if not product or product['quantity'] < item['quantity']:
                return False

        for item in cart_items:
            if not self.catalog_service.reduce_quantity(item['product_id'], item['quantity']):
                return False

        self.data[user_id] = []

        print(f"Поръчка обработена за потребител {user_id}")
        print(f"Адрес: {address}")
        print(f"Плащане: {payment}")
        print(f"Продукти:")
        for item in cart_items:
            print(f"  - {item['name']} ({item['size']}) x{item['quantity']}")

        return True