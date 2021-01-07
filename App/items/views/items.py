"""Items views."""

# Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from ..serializers.items import ItemModelSerializer

# Models
from ..models.items import Item


class ItemsViewSet(viewsets.ModelViewSet):
    """Item view set. """
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to is_active and is_superuser"""
        queryset = Item.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset
