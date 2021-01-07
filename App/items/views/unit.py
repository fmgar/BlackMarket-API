"""Unit views."""

# Django REST framework
from rest_framework import viewsets

# Serializers
from ..serializers.unit import UnitModelSerializer

# Models
from ..models.unit import Unit


class UnitViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Unit.objects.all()
    serializer_class = UnitModelSerializer
