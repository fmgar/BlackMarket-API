"""Items views."""

# Django REST framework
from rest_framework import viewsets

# Serializers
from ..serializers.items import ItemModelSerializer

# Models
from ..models.items import Item


class ItemsViewSet(viewsets.ModelViewSet):
    """Item view set. """
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer
