from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User
from rest_framework.views import View, Request


class Isowner_or_superuser(BasePermission):
    def has_permission(self, request: Request, view: View):

        if request.user.is_authenticated or request.user.is_superuser:
            return True
        return False
