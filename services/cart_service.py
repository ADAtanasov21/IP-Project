from services.catalog_service import CatalogService


class CartService:
    def __init__(self):
        self.carts = {}  # user_id -> list of cart items
        self.catalog_service = CatalogService()

    def add_to_cart(self, user_id, product_id, size):
        if user_id not in self.carts:
            self.carts[user_id] = []

        # Проверяваме дали вече е добавен същия продукт със същия размер
        for item in self.carts[user_id]:
            if item['product_id'] == product_id and item['size'] == size:
                return  # Не добавяме повторно

        product = self.catalog_service.get_product_by_id(product_id)
        if product and product['quantity'] > 0:
            cart_item = {
                'product_id': product_id,
                'name': product['name'],
                'price': product['price'],
                'size': size,
                'image': product['image']
            }
            self.carts[user_id].append(cart_item)

    def get_cart_items(self, user_id):
        return self.carts.get(user_id, [])

    def process_order(self, user_id, address, payment):
        cart_items = self.get_cart_items(user_id)

        # Проверяваме наличността и намаляваме количеството
        for item in cart_items:
            if not self.catalog_service.reduce_quantity(item['product_id']):
                return False

        # Изчистваме кошницата
        self.carts[user_id] = []

        print(f"Поръчка обработена за потребител {user_id}")
        print(f"Адрес: {address}")
        print(f"Плащане: {payment}")

        return True