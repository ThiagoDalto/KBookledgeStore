from django.db import models
import uuid


class Order(models.Model):
    STATUS_CHOICES = [
        (1, ("In process")),
        (2, ("Await payment")),
        (3, ("Completed")),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="order")
    # books = models.ManyToManyField("books.Book", related_name="order")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    on_price = models.DecimalField(max_digits=99, decimal_places=2, default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
