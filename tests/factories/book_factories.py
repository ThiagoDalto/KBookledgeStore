from django.contrib.auth.models import User as UserType
from books.models import Book
from .faker_factory import fake
from authors.models import Author


def create_book(user_book: dict = None, author: Author = Author) -> Book:
    default_book_data = {
        "title": fake.title(),
        "price": fake.price(),
        "page_number": fake.page_number(),
        "synopsis": fake.synopsis(),
        "published_year": fake.published_year(),
        "page_number": fake.page_number(),
        "author": fake.author(),
        "discount": fake.discount(),
        "picture_url": fake.picture_url(),
        # "sales": fake.sales()
    }

    book_data = book_data or default_book_data
    book = Book.objects.create(**book_data)

    return book
