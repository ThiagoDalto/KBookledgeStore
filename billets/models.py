from django.db import models
import uuid


class Billet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="billets",
    )
    barcode = models.CharField(max_length=48)
    value = models.PositiveSmallIntegerField()
    formatted_barcode = models.CharField(max_length=56)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    link_pdf = models.TextField()
    link_png = models.TextField()
