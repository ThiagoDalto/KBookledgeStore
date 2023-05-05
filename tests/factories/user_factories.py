from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserType
from rest_framework_simplejwt.tokens import RefreshToken
from .faker_factory import fake
from authors.models import Author

User: UserType = get_user_model()


def create_user_with_token(
    user_data: dict = None,
    is_superuser: bool = False,
) -> tuple[UserType, str]:
    default_user_data = {
        "username": fake.unique.user_name(),
        "email": fake.unique.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "password": fake.password(),
    }

    user_data = user_data or default_user_data

    if is_superuser:
        user = User.objects.create_superuser(**user_data)
    else:
        user = User.objects.create_user(**user_data)

    user_token = RefreshToken.for_user(user).access_token

    return user, user_token

    def create_user_author(
        author_data: dict = None,
        user: UserType = UserType,
    ) -> Author:
        default_author_data = {"bio": fake.bio(), "user": user}

        author_data = author_data or default_author_data
        author = Author.objects.create(**author_data)
        return author
