""" Owner serializers. """

# Django REST framework
from rest_framework import serializers

# Model
from ..models.owner import Owner


class OwnerModelSerializer(serializers.ModelSerializer):
    """Category model Serializer. """
    class Meta:
        model = Owner
        fields = ['id', 'name']
