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

            # ЗИМНИ ОБУВКИ
            {
                'id': 1, 'name': 'Timberland Boots', 'description': 'Кожени работни обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 220.00,
                'quantity': 8, 'category': 'winter',
                'image': 'https://static.ftshp.digital/img/p/1/2/5/0/8/1/8/1250818-full_product.jpg'
            },
            {
                'id': 2, 'name': 'Dr. Martens 1460', 'description': 'Класически берци с 8 дупки',
                'color': 'Черен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 200.00,
                'quantity': 10, 'category': 'winter',
                'image': 'https://static.ftshp.digital/img/p/4/2/4/5/0/4/424504-full_product.jpg'
            },
            {
                'id': 3, 'name': 'UGG Classic Mini', 'description': 'Топли зимни ботуши',
                'color': 'Кафяв', 'sizes': ['37', '38', '39', '40', '41'], 'price': 280.00,
                'quantity': 12, 'category': 'winter',
                'image': 'https://img.modivo.cloud/product(c/3/6/1/c361a505f35e15104f53efd1c69e7d3bb235cdad_22_0197634331751.jpg,jpg)/ugg-apreski-w-classic-mini-dipper-1168170-kafiav-0000305032843.jpg'
            },
            {
                'id': 4, 'name': 'Sorel Caribou', 'description': 'Водоустойчиви зимни обувки',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 250.00,
                'quantity': 9, 'category': 'winter',
                'image': 'https://static.ftshp.digital/img/p/1/5/5/0/4/5/5/1550455-full_product.jpg'
            },
            {
                'id': 5, 'name': 'Columbia Bugaboot', 'description': 'Зимни туристически обувки',
                'color': 'Сив', 'sizes': ['40', '41', '42', '43', '44'], 'price': 190.00,
                'quantity': 14, 'category': 'winter',
                'image': 'https://m.media-amazon.com/images/I/71+7EjoQXzL._UY900_.jpg'
            },
            {
                'id': 6, 'name': 'Merrell Thermo', 'description': 'Изолирани зимни обувки',
                'color': 'Кафяв', 'sizes': ['39', '40', '41', '42', '43'], 'price': 210.00,
                'quantity': 11, 'category': 'winter',
                'image': 'https://i1.adis.ws/i/jpl/ti_FWWWN2TI0124ALT_a?w=1000&h=1000'
            },

            # СПОРТНИ ОБУВКИ
            {
                'id': 7, 'name': 'Nike Air Max 90', 'description': 'Класически спортни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 180.00,
                'quantity': 15, 'category': 'sport',
                'image': 'https://i8.amplience.net/i/jpl/jd_DH8010-100_C_0010_a?qlt=92'
            },
            {
                'id': 8, 'name': 'Adidas Ultraboost', 'description': 'Бягащи обувки с максимален комфорт',
                'color': 'Черен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 220.00,
                'quantity': 18, 'category': 'sport',
                'image': 'https://static.qns.digital/img/p/2/5/1/8/4/6/8/2518468-full_product.jpg'
            },
            {
                'id': 9, 'name': 'Puma RS-X', 'description': 'Модерни спортни обувки',
                'color': 'Син', 'sizes': ['38', '39', '40', '41', '42'], 'price': 130.00,
                'quantity': 20, 'category': 'sport',
                'image': 'https://i.ebayimg.com/images/g/t3kAAOSwkidkf3Zz/s-l1200.jpg'
            },
            {
                'id': 10, 'name': 'New Balance 574', 'description': 'Ретро бягащи обувки',
                'color': 'Сив', 'sizes': ['39', '40', '41', '42', '43'], 'price': 110.00,
                'quantity': 14, 'category': 'sport',
                'image': 'https://solewhat.com/cdn/shop/files/U574GBG_01_9a388b9d-1778-463a-a239-aa01901e188e.jpg?v=1757563684'
            },
            {
                'id': 11, 'name': 'Asics Gel-Kayano', 'description': 'Професионални бягащи обувки',
                'color': 'Син', 'sizes': ['39', '40', '41', '42', '43'], 'price': 190.00,
                'quantity': 12, 'category': 'sport',
                'image': 'https://cdncloudcart.com/30585/products/images/44256/gel-kayano-31-blue-expansedigital-aqua-665ac88b4b7c2_800x800.jpeg?1717226113'
            },
            {
                'id': 12, 'name': 'Reebok Nano X', 'description': 'Обувки за кросфит и фитнес',
                'color': 'Червен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 160.00,
                'quantity': 16, 'category': 'sport',
                'image': 'https://i.ebayimg.com/images/g/118AAOSwEcplQWml/s-l1200.png'
            },

            # ОФИЦИАЛНИ ОБУВКИ
            {
                'id': 13, 'name': 'Clarks Desert Boot', 'description': 'Елегантни велурени обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 180.00,
                'quantity': 10, 'category': 'formal',
                'image': 'https://cdn.media.amplience.net/i/clarks/26155484_GW_4'
            },
            {
                'id': 14, 'name': 'Oxford Classic', 'description': 'Класически лачени официални обувки',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 220.00,
                'quantity': 8, 'category': 'formal',
                'image': 'https://www.cheaney.co.uk/images/lime-r-classic-oxford-in-black-calf-leather-p35-1278_image.jpg'
            },
            {
                'id': 15, 'name': 'Brogues Premium', 'description': 'Кожени обувки с декорация',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 240.00,
                'quantity': 7, 'category': 'formal',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_g5Qv6BN0-wLDdp1UDyuwIpNIP47hA3ZpeQ&s'
            },
            {
                'id': 16, 'name': 'Derby Elegant', 'description': 'Бизнес обувки от естествена кожа',
                'color': 'Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 200.00,
                'quantity': 11, 'category': 'formal',
                'image': 'https://assets.holyart.it/images/PL007002/us/500/R/SN076398/CLOSEUP04_HD/h-eb2b2d9f/elegant-black-leather-derby-shoe-in-primis.jpg'
            },
            {
                'id': 17, 'name': 'Loafers Suede', 'description': 'Елегантни мокасини от велур',
                'color': 'Синьо', 'sizes': ['40', '41', '42', '43', '44'], 'price': 170.00,
                'quantity': 13, 'category': 'formal',
                'image': 'https://www.loake.com/wp-content/uploads/2023/01/TUSLBS-ANGLE-min.webp'
            },
            {
                'id': 18, 'name': 'Monk Strap Leather', 'description': 'Официални обувки с катарама',
                'color': 'Кафяв', 'sizes': ['39', '40', '41', '42', '43'], 'price': 260.00,
                'quantity': 6, 'category': 'formal',
                'image': 'https://thursdayboots.com/cdn/shop/files/1024x1024-Men-Saint3.0-Cinnamon-070523-3.4_1024x1024.jpg?v=1689006011'
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