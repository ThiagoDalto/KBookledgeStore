from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Promotions

import ipdb

class PromotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotions
        fields = ["id", "name", "starts_at", "ends_at", "updated_at", "book"]
        read_only_fields = ["created_at"]
        extra_kwargs = {
            'validators': [UniqueValidator(queryset=Promotions.objects.all())] 
        }
        
        

    def create(self, validated_data: dict) -> Promotions:

        books = validated_data.pop("book")

        promotions = Promotions.objects.create(**validated_data)

        promotions.book.set(books)

        return promotions

    def update(self, instance: Promotions, validated_data: dict ) -> Promotions:

        books = validated_data.pop("book")
        instance.book.set(books)
        
        for key, value in validated_data.items():
            setattr( instance, key, value )

        instance.save()

        return instance

