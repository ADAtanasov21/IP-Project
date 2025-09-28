class CatalogService:
    def __init__(self):
        self.products = [
            {
                'id': 1, 'name': 'Nike Air Max 90', 'description': 'Класически спортни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 180.00,
                'quantity': 15, 'image': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400'
            },
            {
                'id': 2, 'name': 'Adidas Stan Smith', 'description': 'Минимални бели кецове',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 120.00,
                'quantity': 20, 'image': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400'
            },
            {
                'id': 3, 'name': 'Converse Chuck Taylor', 'description': 'Високи кецове в червено',
                'color': 'Червен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 85.00,
                'quantity': 12, 'image': 'https://images.unsplash.com/photo-1514989940723-e8e51635b782?w=400'
            },
            {
                'id': 4, 'name': 'Timberland Boots', 'description': 'Кожени работни обувки',
                'color': 'Кафяв', 'sizes': ['40', '41', '42', '43', '44'], 'price': 220.00,
                'quantity': 8, 'image': 'https://images.unsplash.com/photo-1520639888713-7851133b1ed0?w=400'
            },
            {
                'id': 5, 'name': 'Vans Old Skool', 'description': 'Скейт обувки с классическа ивица',
                'color': 'Черен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 95.00,
                'quantity': 18, 'image': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400'
            },
            {
                'id': 6, 'name': 'New Balance 574', 'description': 'Ретро бягащи обувки',
                'color': 'Сив', 'sizes': ['39', '40', '41', '42', '43'], 'price': 110.00,
                'quantity': 14, 'image': 'https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=400'
            },
            {
                'id': 7, 'name': 'Jordan 1 High', 'description': 'Икона на баскетболните обувки',
                'color': 'Черен', 'sizes': ['40', '41', '42', '43', '44'], 'price': 320.00,
                'quantity': 6, 'image': 'https://images.unsplash.com/photo-1556906781-9a412961c28c?w=400'
            },
            {
                'id': 8, 'name': 'Puma Suede Classic', 'description': 'Велурени спортни обувки',
                'color': 'Син', 'sizes': ['38', '39', '40', '41', '42'], 'price': 75.00,
                'quantity': 22, 'image': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400'
            },
            {
                'id': 9, 'name': 'Dr. Martens 1460', 'description': 'Класически берци с 8 дупки',
                'color': 'Черен', 'sizes': ['37', '38', '39', '40', '41'], 'price': 200.00,
                'quantity': 10, 'image': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400'
            },
            {
                'id': 10, 'name': 'Reebok Classic', 'description': 'Бели кожени кецове',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 90.00,
                'quantity': 16, 'image': 'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400'
            },
            {
                'id': 11, 'name': 'Nike Blazer Mid', 'description': 'Високи баскетболни обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 140.00,
                'quantity': 13, 'image': 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?w=400'
            },
            {
                'id': 12, 'name': 'Asics Gel-Lyte III', 'description': 'Ретро бягащи обувки',
                'color': 'Зелен', 'sizes': ['38', '39', '40', '41', '42'], 'price': 130.00,
                'quantity': 11, 'image': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400'
            },
            {
                'id': 13, 'name': 'Balenciaga Triple S', 'description': 'Луксозни chunky обувки',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 890.00,
                'quantity': 4, 'image': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=400'
            },
            {
                'id': 14, 'name': 'Salomon Speedcross', 'description': 'Планински обувки за бягане',
                'color': 'Сив', 'sizes': ['40', '41', '42', '43', '44'], 'price': 160.00,
                'quantity': 9, 'image': 'https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=400'
            },
            {
                'id': 15, 'name': 'Fila Disruptor II', 'description': 'Chunky dad обувки',
                'color': 'Бял', 'sizes': ['37', '38', '39', '40', '41'], 'price': 110.00,
                'quantity': 17, 'image': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400'
            },
            {
                'id': 16, 'name': 'Golden Goose Superstar', 'description': 'Луксозни vintage обувки',
                'color': 'Бял', 'sizes': ['38', '39', '40', '41', '42'], 'price': 450.00,
                'quantity': 7, 'image': 'https://images.unsplash.com/photo-1529810313688-44ea1c2d81d3?w=400'
            },
            {
                'id': 17, 'name': 'Yeezy Boost 350', 'description': 'Adidas x Kanye West колаборация',
                'color': 'Розов', 'sizes': ['39', '40', '41', '42', '43'], 'price': 380.00,
                'quantity': 5, 'image': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400'
            },
            {
                'id': 18, 'name': 'Common Projects Achilles', 'description': 'Минимални луксозни кецове',
                'color': 'Бял', 'sizes': ['39', '40', '41', '42', '43'], 'price': 420.00,
                'quantity': 8, 'image': 'https://images.unsplash.com/photo-1595341888016-a392ef81b7de?w=400'
            },
            {
                'id': 19, 'name': 'Off-White Jordan 1', 'description': 'Колаборация с Virgil Abloh',
                'color': 'Оранжев', 'sizes': ['40', '41', '42', '43', '44'], 'price': 750.00,
                'quantity': 3, 'image': 'https://images.unsplash.com/photo-1607522370275-f14206abe5d3?w=400'
            },
            {
                'id': 20, 'name': 'Allbirds Tree Runners', 'description': 'Екологични обувки от мерино',
                'color': 'Сив', 'sizes': ['38', '39', '40', '41', '42'], 'price': 150.00,
                'quantity': 12, 'image': 'https://images.unsplash.com/photo-1554735490-5974588f3909?w=400'
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