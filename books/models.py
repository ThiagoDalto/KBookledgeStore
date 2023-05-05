from django.db import models
import uuid

# cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    price = models.IntegerField()
    page_number = models.IntegerField()
    synopsis = models.TextField()
    published_year = models.IntegerField()
    page_number = models.IntegerField()
    author = models.ForeignKey(
        "authors.Author", on_delete=models.CASCADE, related_name="books"
    )
    pdf_book = models.FileField(max_length=30)
    discount = models.IntegerField(null=True)
    on_sale = models.BooleanField(default=False)
    sales = models.IntegerField(default=0)
    picture_url = CloudinaryField('imagem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categorys = models.ManyToManyField("books.Category", related_name="books")

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)