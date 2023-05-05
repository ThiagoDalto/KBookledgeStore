from rest_framework import serializers
from .models import Order
from books.models import Book
import ipdb
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 1
        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        book_id = validated_data["book_id"]
        book = get_object_or_404(Book, pk=book_id)

        order = Order.objects.create(**validated_data)
        
        if book.on_sale:
            discont_price = book.price * (1 - (book.discount / 100))
            order.on_price += discont_price
        else:
            order.on_price += book.price
        order.save()
        
        return order

    def update(self, instance, validated_data):
        books = validated_data.pop("books")
