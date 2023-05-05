from rest_framework import permissions
from .models import User
from rest_framework.views import View
from rest_framework.request import Request

class IsAccountOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        
        if  request.user.is_superuser :
            return True
        
        return request.user.is_authenticated and obj == request.user

class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request:Request, view):

        if request._request.method == "GET":
            return bool(request.user and request.user.is_authenticated)

        return True

        

