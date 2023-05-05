from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Author


class AuthorsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Author.objects.all(),
                message="A author with that name already exists."
            )
        ]
    )

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'bio',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
