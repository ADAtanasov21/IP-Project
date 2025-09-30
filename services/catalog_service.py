class BaseService:

    def __init__(self):
        self.data = []
        self.next_id = 1

    def get_all(self):
        return self.data

    def get_by_id(self, item_id):
        return next((item for item in self.data if item['id'] == item_id), None)


class CatalogService(BaseService):
    def __init__(self):
        super().__init__()
        self.data = [

            {
                'id': 1, 'name': 'Timberland Boots', 'description': 'Кожени работни обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 220.00,
                'quantity': 8, 'category': 'winter',
                'image': 'https://images.unsplash.com/photo-1520639888713-7851133b1ed0?w=400'
            },
            {
                'id': 2, 'name': 'Dr. Martens 1460', 'description': 'Класически берци с 8 дупки',
                'color': 'Черен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 200.00,
                'quantity': 10, 'category': 'winter',
                'image': 'https://static.ftshp.digital/img/p/4/2/4/5/1/9/424519-full_product.jpg'
            },
            {
                'id': 3, 'name': 'UGG Classic Mini', 'description': 'Топли зимни ботуши',
                'color': 'Кафяв', 'sizes': ['37', '38', '39', '40', '41'], 'price': 280.00,
                'quantity': 12, 'category': 'winter',
                'image': 'https://images.ugg.com/is/image/UGGAustralia/1016222-CHE-HERO?$product-gallery-zoom$'
            },
            {
                'id': 4, 'name': 'Sorel Caribou', 'description': 'Водоустойчиви зимни обувки',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 250.00,
                'quantity': 9, 'category': 'winter',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYxK8vK9zY9VhJXz_QxG5R8xJ8dKJxYzxJjA&s'
            },
            {
                'id': 5, 'name': 'Columbia Bugaboot', 'description': 'Зимни туристически обувки',
                'color': 'Сив', 'sizes': ['40', '41', '42', '43', '44'], 'price': 190.00,
                'quantity': 14, 'category': 'winter',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgT5xK3QxZ3zF8vJK8wH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 6, 'name': 'Merrell Thermo', 'description': 'Изолирани зимни обувки',
                'color': 'Кафяв', 'sizes': ['39', '40', '41', '42', '43'], 'price': 210.00,
                'quantity': 11, 'category': 'winter',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },

            {
                'id': 7, 'name': 'Nike Air Max 90', 'description': 'Класически спортни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 180.00,
                'quantity': 15, 'category': 'sport',
                'image': 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/zwxes8uud05rkuei1mpt/AIR+MAX+90.png'
            },
            {
                'id': 8, 'name': 'Adidas Ultraboost', 'description': 'Бягащи обувки с максимален комфорт',
                'color': 'Черен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 220.00,
                'quantity': 18, 'category': 'sport',
                'image': 'https://assets.adidas.com/images/w_600,f_auto,q_auto/8a2d1f6cd3984e67a896ad7e00e8c7f2_9366/Ultraboost_Light_Shoes_Black_GY9350_01_standard.jpg'
            },
            {
                'id': 9, 'name': 'Puma RS-X', 'description': 'Модерни спортни обувки',
                'color': 'Син', 'sizes': ['38', '39', '40', '41', '42'], 'price': 130.00,
                'quantity': 20, 'category': 'sport',
                'image': 'https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_2000,h_2000/global/380462/01/sv01/fnd/PNA/fmt/png/RS-X-Reinvention-Sneakers'
            },
            {
                'id': 10, 'name': 'New Balance 574', 'description': 'Ретро бягащи обувки',
                'color': 'Сив', 'sizes': ['39', '40', '41', '42', '43'], 'price': 110.00,
                'quantity': 14, 'category': 'sport',
                'image': 'https://static.ftshp.digital/img/p/1/1/7/8/1/9/4/1178194-full_product.jpg'
            },
            {
                'id': 11, 'name': 'Asics Gel-Kayano', 'description': 'Професионални бягащи обувки',
                'color': 'Син', 'sizes': ['39', '40', '41', '42', '43'], 'price': 190.00,
                'quantity': 12, 'category': 'sport',
                'image': 'https://images.asics.com/is/image/asics/1011B630_400_SR_RT_GLB?$zoom$'
            },
            {
                'id': 12, 'name': 'Reebok Nano X', 'description': 'Обувки за кросфит и фитнес',
                'color': 'Червен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 160.00,
                'quantity': 16, 'category': 'sport',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },

            {
                'id': 13, 'name': 'Clarks Desert Boot', 'description': 'Елегантни велурени обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 180.00,
                'quantity': 10, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 14, 'name': 'Oxford Classic', 'description': 'Класически лачени официални обувки',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 220.00,
                'quantity': 8, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 15, 'name': 'Brogues Premium', 'description': 'Кожени обувки с декорация',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 240.00,
                'quantity': 7, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 16, 'name': 'Derby Elegant', 'description': 'Бизнес обувки от естествена кожа',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 200.00,
                'quantity': 11, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 17, 'name': 'Loafers Suede', 'description': 'Елегантни мокасини от велур',
                'color': 'Синьо', 'sizes': ['40', '41', '42', '43', '44'], 'price': 170.00,
                'quantity': 13, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            },
            {
                'id': 18, 'name': 'Monk Strap Leather', 'description': 'Официални обувки с катарама',
                'color': 'Кафяв', 'sizes': ['39', '40', '41', '42', '43'], 'price': 260.00,
                'quantity': 6, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxK9xH3xK9xH3xK9xH3xK9xH3xK9xH3xK9xH&s'
            }
        ]
        self.next_id = 19

    def get_all(self, category=None):
        if category:
            return [p for p in self.data if p['category'] == category]
        return super().get_all()

    def get_products(self, category=None):
        return self.get_all(category)

    def get_product_by_id(self, product_id):
        return self.get_by_id(product_id)

    def add_product(self, product_data):
        product = {
            'id': self.next_id,
            **product_data
        }
        self.data.append(product)
        self.next_id += 1

    def update_product(self, product_id, product_data):
        product = self.get_by_id(product_id)
        if product:
            product.update(product_data)

    def delete_product(self, product_id):
        self.data = [p for p in self.data if p['id'] != product_id]

    def reduce_quantity(self, product_id, amount=1):
        product = self.get_by_id(product_id)
        if product and product['quantity'] >= amount:
            product['quantity'] -= amount
            return True
        return False