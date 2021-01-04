"""Users serializers. """

# Django REST framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

# Models
from App.users.models import User, Profile


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
            'is_verified',
            'is_staff'
        )


class UserSignUpSerializer(serializers.Serializer):
    """User sig up serializer. 

    Handle sign up data validation and user/profile creation.
    """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=15,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999."
    )

    phone_number = serializers.CharField(validators=[phone_regex])

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Password don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user profile creation. """
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)
        return user


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
