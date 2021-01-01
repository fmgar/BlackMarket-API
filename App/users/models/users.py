"""User model. """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from App.utils.models import BlackMarketModel


class User(BlackMarketModel, AbstractUser):
    """User model.

    Extend from Django's Abstrac User, change the username field
    to email and add some extra fields. """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999."
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_superuser = models.BooleanField(
        'superuser',
        default=False,
        help_text=(
            'If is True the user can read, edit and delete data. If es false the user only can read data'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address'
    )

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        return self.username
