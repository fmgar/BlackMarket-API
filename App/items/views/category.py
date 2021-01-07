"""Category views."""

# Django REST framework
from rest_framework import viewsets

# Serializers
from ..serializers.category import CategoryModelSerializer

# Models
from ..models.category import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
