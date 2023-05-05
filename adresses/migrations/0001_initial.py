from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("country", models.CharField(default="Brasil", max_length=64)),
                ("state", models.CharField(max_length=64, null=True)),
                ("city", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "neighborhood",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "street_address",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                ("zip_code", models.CharField(max_length=9)),
                ("uf", models.CharField(blank=True, max_length=4, null=True)),
                ("complement", models.TextField(blank=True, null=True)),
                ("number", models.CharField(default="S/N", max_length=10)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
        ),
    ]
