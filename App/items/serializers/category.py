""" Category serializers. """

# Django REST framework
from rest_framework import serializers

# Model
from ..models.category import Category


class CategoryModelSerializer(serializers.ModelSerializer):
    """Category model Serializer. """
    class Meta:
        model = Category
        fields = ['id', 'name']
