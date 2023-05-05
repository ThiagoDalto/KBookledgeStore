from django.db import models
from uuid import uuid4
from users.models import User
# Create your models here.


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    name = models.CharField(max_length=128)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User)
