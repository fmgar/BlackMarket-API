"""Users serializers. """

# Django REST framework
from rest_framework import serializers

# Django
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login data."""

    email = serializers.EmailField()
    passworkd = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials. """
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return data
