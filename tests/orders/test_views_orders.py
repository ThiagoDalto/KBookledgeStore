from rest_framework.test import APITestCase
from rest_framework.views import status
from tests.factories import (book_factories, user_factories)


class OrderCreateViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/books/order/"
        cls.BASE_DETAIL_URL = cls.BASE_URL + "1/"
        cls.user, cls.token = user_factories()
        cls.book = book_factories()

    def test_create_order_without_token(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code

        msg = (
            "\nCheck if status code POST request without token "
            + f"in `{self.BASE_URL}` is {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)

    def test_create_order_with_token(self):
        order_data = {
            "book_id": self.book,
            "user": self.user,
        }
        self.client.credentials(HTTP_AUTHORIZATION="Baerer" + self.token)
        response = self.client.post(self.BASE_URL, data=order_data, format="json")

        expected_status_code = status.HTTP_201_CREATED
        resulted_status_code = response.status_code

        msg = (
            "\nCheck if status code POST request with token "
            + f"in `{self.BASE_URL}` is {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)

    def test_create_order_with_invalid_token(self):
        order_data = {
            "book_id": self.book,
            "user": self.user,
        }
        self.client.credentials(HTTP_AUTHORIZATION="Bearer" + "invalid token")
        response = self.client.post(self.BASE_URL, data=order_data, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code

        msg = (
            "\nCheck if status code POST request with invalid token "
            + f"in `{self.BASE_URL}` is {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)

    def test_create_order_with_not_found_book_uuid(self):
        order_data = {
            "book_id": "invalid book",
            "user": self.user,
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(self.BASE_URL, data=order_data, format="json")

        # RETORNO JSON
        resulted_data = response.json()
        expected_data = {"detail": "Not found."}

        msg = (
            "check if message with invalid book_id at POST "
            + f"in `{self.BASE_URL}` is correct."
        )
        self.assertDictEqual(expected_data, resulted_data)

        expected_status_code = status.HTTP_404_NOT_FOUND
        resulted_status_code = response.status_code
        msg = (
            "\nCheck if status code at POST "
            + f"in `{self.BASE_URL}` with invalid book_id is {expected_status_code}."
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)
