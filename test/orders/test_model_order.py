from django.test import TestCase
from orders.models import Order
from books.models import Book
from users.models import User


class OrderModelTest(TestCase):
    @classmethod
    def test_check_relationship_with_user(self):
        relationship = Order._meta.get_field("user").is_relation
        self.assertTrue(relationship, "Don't have relatioship with User")

    def test_check_relationship_with_book(self):
        relationship = Order._meta.get_field("book").is_relation
        self.assertTrue(relationship, "Don't have relatioship with Book")

    def test_check_if_status_gets_only_three_possibilities(self):
        choices_amount = len(Order._meta.get_field("status").choices)
        self.assertEqual(choices_amount, 3, msg="Don't have 3 choices")

    def test_check_status_name_possibilities(self):
        choices = Order._meta.get_field("status").choices
        self.assertEqual(choices[0][1], 'In process', msg="Name is not 'In process'")
        self.assertEqual(choices[1][1], 'Await payment', msg="Name is not 'Await payment'")
        self.assertEqual(choices[2][1], 'Completed', msg="Name is not 'Completed'")
