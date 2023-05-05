from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Billet",
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
                ("barcode", models.CharField(max_length=48)),
                ("value", models.PositiveSmallIntegerField()),
                ("formatted_barcode", models.CharField(max_length=56)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("due_date", models.DateTimeField()),
                ("link_pdf", models.TextField()),
                ("link_png", models.TextField()),
            ],
        ),
    ]
