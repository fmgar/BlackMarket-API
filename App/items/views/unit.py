"""Unit views."""

# Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from ..serializers.unit import UnitModelSerializer

# Models
from ..models.unit import Unit


class UnitViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Unit.objects.all()
    serializer_class = UnitModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to is_active and is_superuser"""
        queryset = Unit.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset
