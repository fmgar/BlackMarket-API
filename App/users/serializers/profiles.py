"""Profile serializer. """

# Django REST Framework
from rest_framework import serializers

# Models
from App.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    class Meta:
        model = Profile
        fields = (
            'picture',
            'biography'
        )
