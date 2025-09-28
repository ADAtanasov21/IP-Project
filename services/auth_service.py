from flask import session

users = []
user_id_counter = 1


def register_user(email, password, name):
    global user_id_counter

    for user in users:
        if user['email'] == email:
            return False

    user = {
        'id': user_id_counter,
        'email': email,
        'password': password,  # In real app, hash this!
        'name': name,
        'is_admin': False
    }

    users.append(user)
    user_id_counter += 1

    print(f"Email sent to {email}: Registration confirmed!")

    return True


def login_user(email, password):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user
    return None


def logout_user():
    session.clear()


def create_admin_user():
    admin = {
        'id': 999,
        'email': 'admin@shoestore.com',
        'password': 'admin123',
        'name': 'Administrator',
        'is_admin': True
    }

    if not any(user['email'] == admin['email'] for user in users):
        users.append(admin)
        print("Admin user created: admin@shoestore.com / admin123")