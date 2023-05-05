from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .permissions import IsOwner
from .serializers import OrderSerializer
from books.models import Book
from .models import Order
import ipdb
import json


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated, IsOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        book_id = self.kwargs["pk"]
        serializer.save(user=self.request.user, book_id=book_id)


class OrderIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
