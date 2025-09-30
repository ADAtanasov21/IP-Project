class BaseService:

    def __init__(self):
        self.data = []
        self.next_id = 1

    def get_all(self):
        return self.data

    def get_by_id(self, item_id):
        return next((item for item in self.data if item['id'] == item_id), None)

class AuthService(BaseService):
    def __init__(self):
        super().__init__()
        self.data = [
            {'id': 1, 'email': 'admin@shop.com', 'password': 'admin123', 'is_admin': True},
            {'id': 2, 'email': 'user1@shop.com', 'password': 'user123', 'is_admin': False},
            {'id': 3, 'email': 'user2@shop.com', 'password': 'user456', 'is_admin': False}
        ]
        self.next_id = 4

    def get_by_id(self, user_id):

        user = super().get_by_id(user_id)
        if user:

            return {'id': user['id'], 'email': user['email'], 'is_admin': user['is_admin']}
        return None

    def register_user(self, email, password):
        if any(user['email'] == email for user in self.data):
            return False

        new_user = {
            'id': self.next_id,
            'email': email,
            'password': password,
            'is_admin': False
        }
        self.data.append(new_user)
        self.next_id += 1
        return True

    def login_user(self, email, password):
        for user in self.data:
            if user['email'] == email and user['password'] == password:
                return user
        return None