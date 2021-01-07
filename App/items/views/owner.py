"""Owner views."""

# Django REST framework
from rest_framework import viewsets

# Serializers
from ..serializers.owner import OwnerModelSerializer

# Models
from ..models.owner import Owner


class OwnerViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Owner.objects.all()
    serializer_class = OwnerModelSerializer
