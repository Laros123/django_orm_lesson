import django_setup
from app_construct.models import User


def init():
    admin = User(
        login='admin',
        email='superadmin@gmail.com',
        role='admin'
    )
    admin.save()

    user = User(
        login='user',
        email='user1@gmail.com',
        role='user'
    )
    user.save()

def main():
    init()

if __name__ == "__main__":
    main()
