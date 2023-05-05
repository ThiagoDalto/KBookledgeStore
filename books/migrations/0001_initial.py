import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=32, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=128)),
                ("price", models.IntegerField()),
                ("synopsis", models.TextField()),
                ("published_year", models.IntegerField()),
                ("page_number", models.IntegerField()),
                ("pdf_book", models.FileField(max_length=30, upload_to="")),
                ("discount", models.IntegerField(null=True)),
                ("on_sale", models.BooleanField(default=False)),
                ("sales", models.IntegerField(default=0)),
                (
                    "picture_url",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="imagem"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="authors.author",
                    ),
                ),
                (
                    "categorys",
                    models.ManyToManyField(related_name="books", to="books.category"),
                ),
            ],
        ),
    ]
