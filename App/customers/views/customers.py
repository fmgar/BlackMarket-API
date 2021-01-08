""""Customers views."""

# Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from App.customers.serializers.customers import CustomerModelSerializer

# Models
from App.customers.models.customers import Customer


class CustomersViewSet(viewsets.ModelViewSet):
    """Customers view set. """
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to is_active and is_superuser"""
        queryset = Customer.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset
