""" Unit serializers. """

# Django REST framework
from rest_framework import serializers

# Model
from ..models.unit import Unit


class UnitModelSerializer(serializers.ModelSerializer):
    """Category model Serializer. """
    class Meta:
        model = Unit
        fields = ['id', 'name']
