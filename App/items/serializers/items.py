""" Items serializers. """

# Django REST framework
from rest_framework import serializers

# Model
from ..models.items import Item
from ..models.category import Category
from ..serializers.category import CategoryModelSerializer


class ItemModelSerializer(serializers.ModelSerializer):
    """Item model Serializer. """

    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'category',
            'description',
            'type_item',
            'unit',
            'price',
            'owner'

        ]
