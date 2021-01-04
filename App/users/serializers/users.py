"""Users serializers. """

# Django REST framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Django
from django.contrib.auth import authenticate

# Models
from App.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_superuser',
            'is_verified'
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login data."""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials. """
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrive new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
