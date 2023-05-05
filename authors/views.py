from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorsSerializer
from .models import Author
from books.models import Book
from .permissions import Isowner_or_superuser


class AuthorsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [Isowner_or_superuser, BasePermission]
    serializer_class = AuthorsSerializer

    queryset = Author.objects.all()

class AuthorsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [Isowner_or_superuser, BasePermission]
    
    serializer_class = AuthorsSerializer
    queryset = Author.objects.all()

