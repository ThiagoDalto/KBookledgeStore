from rest_framework import permissions
import ipdb
from .models import Order


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj=Order):
        if request.user.is_superuser:
            return True

        for book in obj:
            return book.user == request.user
