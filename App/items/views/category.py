"""Category views."""

# Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from ..serializers.category import CategoryModelSerializer

# Models
from ..models.category import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """Category view set. """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to is_active and is_superuser"""
        queryset = Category.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset
