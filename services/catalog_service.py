class CatalogService:
    def __init__(self):
        self.products = [
            {
                'id': 1, 'name': 'Nike Air Max 90', 'description': 'Класически спортни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 180.00,
                'quantity': 15, 'image': 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/zwxes8uud05rkuei1mpt/AIR+MAX+90.png'
            },
            {
                'id': 2, 'name': 'Adidas Stan Smith', 'description': 'Минимални бели кецове',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 120.00,
                'quantity': 20, 'image': 'https://hiii-style.com/cdn/shop/files/0f66116d-4dc8-4e3c-a446-cca03a5355a7.jpg?v=1736527892&width=1445'
            },
            {
                'id': 3, 'name': 'Converse Chuck Taylor', 'description': 'Високи кецове в червено',
                'color': 'Червен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 85.00,
                'quantity': 12, 'image': 'https://backend.shooos.eu/media/catalog/product/cache/4c418495417d2157523b2d52700ac77f/c/o/converse-chuck-taylor-all-star-hi-red-11_c1fnbxtgnvbgyy7y.jpg'
            },
            {
                'id': 4, 'name': 'Timberland Boots', 'description': 'Кожени работни обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 220.00,
                'quantity': 8, 'image': 'https://images.unsplash.com/photo-1520639888713-7851133b1ed0?w=400'
            },
            {
                'id': 5, 'name': 'Vans Old Skool', 'description': 'Скейт обувки с классическа ивица',
                'color': 'Черен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 95.00,
                'quantity': 18, 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiK9orHDqwBeXtaQJNhmB0hBL1eNrTYSkDZA&s'
            },
            {
                'id': 6, 'name': 'New Balance 574', 'description': 'Ретро бягащи обувки',
                'color': 'Сив', 'sizes': ['39', '40', '41', '42', '43'], 'price': 110.00,
                'quantity': 14, 'image': 'https://static.ftshp.digital/img/p/1/1/7/8/1/9/4/1178194-full_product.jpg'
            },
            {
                'id': 7, 'name': 'Jordan 1 High', 'description': 'Икона на баскетболните обувки',
                'color': 'Червен', 'sizes': ['40', '41', '42', '43', '44'], 'price': 320.00,
                'quantity': 6, 'image': 'https://static.flexdog.bg/flexdog-5/products/images/03cf74ed-4d27-4acb-a0f4-c94b128bf3af.jpeg?width=750&quality=40'
            },
            {
                'id': 8, 'name': 'Puma Suede Classic', 'description': 'Велурени спортни обувки',
                'color': 'Син', 'sizes': ['38', '39', '40', '41', '42'], 'price': 75.00,
                'quantity': 22, 'image': 'https://img.eobuwie.cloud/eob_product_660w_880h(c/c/a/3/cca3a81de28cd10e06e4d38b52b487819b7260db_0000199377860_puma_352634_64_anp_02,jpg)/snikrsi-puma-suede-classic-352634-64-olympian-blue-white.jpg'
            },
            {
                'id': 9, 'name': 'Dr. Martens 1460', 'description': 'Класически берци с 8 дупки',
                'color': 'Черен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 200.00,
                'quantity': 10, 'image': 'https://static.ftshp.digital/img/p/4/2/4/5/1/9/424519-full_product.jpg'
            },
            {
                'id': 10, 'name': 'Reebok Classic', 'description': 'Бели кожени кецове',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 90.00,
                'quantity': 16, 'image': 'https://static.ftshp.digital/img/p/8/2/7/1/8/2/827182-full_product.jpg'
            },
            {
                'id': 11, 'name': 'Nike Blazer Mid', 'description': 'Високи баскетболни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 140.00,
                'quantity': 13, 'image': 'https://static.ftshp.digital/img/p/9/9/7/3/4/8/997348-full_product.jpg'
            },
            {
                'id': 12, 'name': 'Asics Gel-Lyte III', 'description': 'Ретро бягащи обувки',
                'color': 'Зелен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 130.00,
                'quantity': 11, 'image': 'https://images.asics.com/is/image/asics/1201A809_300_SR_RT_GLB?$sfcc-product$'
            },
            {
                'id': 13, 'name': 'Balenciaga Triple S', 'description': 'Луксозни chunky обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 890.00,
                'quantity': 4, 'image': 'https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2019%2F08%2Fbalenciaga-triple-s-pearl-grey-release-11.jpg?q=75&w=800&cbr=1&fit=max'
            },
            {
                'id': 14, 'name': 'Salomon Speedcross', 'description': 'Планински обувки за бягане',
                'color': 'Сив', 'sizes': ['40', '41', '42', '43', '44'], 'price': 160.00,
                'quantity': 9, 'image': 'https://www.evelostore.com/56628-large_default/salomon-trail-running-shoes-speedcross-5-grey.jpg'
            },
            {
                'id': 15, 'name': 'Fila Disruptor II', 'description': 'Chunky dad обувки',
                'color': 'Бял', 'sizes': ['37', '38', '39', '40', '41'], 'price': 110.00,
                'quantity': 17, 'image': 'https://static.ftshp.digital/img/p/2/1/7/4/6/1/217461-full_product.jpg'
            },
            {
                'id': 16, 'name': 'Golden Goose Superstar', 'description': 'Луксозни vintage обувки',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 450.00,
                'quantity': 7, 'image': 'https://cdn.nextchapter-ecommerce.com/Public/Products/xlarge/12342366-94940-golden-goose-sneaker-superstar-white-platinum-grey-10.jpg'
            },
            {
                'id': 17, 'name': 'Yeezy Boost 350', 'description': 'Adidas x Kanye West колаборация',
                'color': ' Черен', 'sizes': ['39', '40', '41', '42', '43'], 'price': 380.00,
                'quantity': 5, 'image': 'https://kickhaven.eu/cdn/shop/files/yeezy-boost-350-v2-reflective-black-static-FU9007_3.webp?v=1752613035&width=1024'
            },
            {
                'id': 18, 'name': 'Common Projects Achilles', 'description': 'Минимални луксозни кецове',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 420.00,
                'quantity': 8, 'image': 'https://www.careofcarl.com/bilder/artiklar/zoom/14839911r_3.jpg?m=1757591583'
            },
            {
                'id': 19, 'name': 'Off-White Jordan 1', 'description': 'Колаборация с Virgil Abloh',
                'color': 'Оранжев', 'sizes': ['Няма налични бройки'], 'price': 750.00,
                'quantity': 0, 'image': 'https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2022%2F02%2Fzach-lavine-commissions-custom-off-white-x-air-jordan-1-low-starfish-000.jpg?w=960&cbr=1&q=90&fit=max'
            },
            {
                'id': 20, 'name': 'Allbirds Tree Runners', 'description': 'Екологични обувки от мерино',
                'color': 'Сив', 'sizes': ['Няма налични бройки'], 'price': 150.00,
                'quantity': 0, 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaIq3mhZQkgBm2SXcj8HHUaYq5wOs8gVufzw&s'
            }
        ]
        self.next_id = 21

    def get_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        return next((p for p in self.products if p['id'] == product_id), None)

    def add_product(self, product_data):
        product = {
            'id': self.next_id,
            **product_data
        }
        self.products.append(product)
        self.next_id += 1

    def update_product(self, product_id, product_data):
        product = self.get_product_by_id(product_id)
        if product:
            product.update(product_data)

    def delete_product(self, product_id):
        self.products = [p for p in self.products if p['id'] != product_id]

    def reduce_quantity(self, product_id, amount=1):
        product = self.get_product_by_id(product_id)
        if product and product['quantity'] >= amount:
            product['quantity'] -= amount
            return True
        return False