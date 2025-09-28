class AuthService:
    def __init__(self):
        self.users = [
            {'id': 1, 'email': 'admin@shop.com', 'password': 'admin123', 'is_admin': True},
            {'id': 2, 'email': 'user1@shop.com', 'password': 'user123', 'is_admin': False},
            {'id': 3, 'email': 'user2@shop.com', 'password': 'user456', 'is_admin': False}
        ]
        self.next_id = 4

    def register_user(self, email, password):
        if any(user['email'] == email for user in self.users):
            return False

        new_user = {
            'id': self.next_id,
            'email': email,
            'password': password,
            'is_admin': False
        }
        self.users.append(new_user)
        self.next_id += 1
        return True

    def login_user(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                return user
        return None