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
        fields = [
            'id',
            'first_name',
            'last_name',
            'ident',
            'phone',
            'email',
            "address",
            "district",
            "reference",
            "birthday"
        ]
