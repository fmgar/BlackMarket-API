"""Circle serializers. """

# Django REST framework
from rest_framework import serializers

# Model
from App.customers.models.customers import Customer


class CustomerModelSerializer(serializers.ModelSerializer):
    """Circle model serializer. """

    class Meta:
        """Meta class. """
        model = Customer
        fields = '__all__'
