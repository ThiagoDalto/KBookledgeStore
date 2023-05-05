from rest_framework import serializers

from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = '__all__'
            depth = 1

    def to_representation(self, instance):
        representation = super(BookSerializer, self).to_representation(instance)
        representation['picture_url'] = instance.picture_url.url
        return representation


class BookPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = '__all__'

    def create(self, validated_data):
        categorys = validated_data.pop("categorys")

        created_book = Book.objects.create(**validated_data)
        created_book.categorys.set(categorys)
        return created_book

    def update(self, instance, validated_data):
        try:
            categorys = validated_data.pop("categorys")
            instance.categorys.set(categorys)
        except KeyError:
            pass
        
        for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        
        return instance

    def to_representation(self, instance):
        representation = super(BookPostUpdateSerializer, self).to_representation(instance)
        representation['picture_url'] = instance.picture_url.url
        return representation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = '__all__'