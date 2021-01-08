"""Owner views."""

# Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from ..serializers.owner import OwnerModelSerializer

# Models
from ..models.owner import Owner


class OwnerViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Owner.objects.all()
    serializer_class = OwnerModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to is_active and is_superuser"""
        queryset = Owner.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset
