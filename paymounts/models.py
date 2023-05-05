from django.db import models
import uuid


class Paymount(models.Model):
    PAYMOUNT_METHOD_CHOICES = [
        (1, ("BOLETO")),
        (2, ("CREDIT_CARD")),
        (3, ("DEBIT_CARD")),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    reference = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="paymounts",
    )
    billet = models.OneToOneField(
        "billets.Billet", on_delete=models.CASCADE, related_name="paymount", null=True,
    )
    description = models.TextField(max_length=64, null=True)
    status = models.CharField(max_length=64)
    value = models.PositiveSmallIntegerField()
    payment_method = models.CharField(max_length=64, choices=PAYMOUNT_METHOD_CHOICES, default=1)
    created_at = models.DateTimeField()
    paid_at = models.DateTimeField(null=True)
    card = models.CharField(max_length=7, null=True)

    link_billet_pdf = models.TextField()
    link_billet_png = models.TextField()
    # updated_at = models.DateTimeField(auto_now=True)
