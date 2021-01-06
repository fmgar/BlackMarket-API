""""Customers views."""

# Django REST framework
from rest_framework import viewsets

# Serializers
from App.customers.serializers.customers import CustomerModelSerializer

# Models
from App.customers.models.customers import Customer


class CustomersViewSet(viewsets.ModelViewSet):
    """Customers view set. """
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
