"""Customers model. """

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from App.utils.models import BlackMarketModel


class Customer(BlackMarketModel):
    """ Customer Model.

    Is a model where save all clients of our application"""

    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=True)
    identification = models.IntegerField(blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999."
    )

    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    email = models.EmailField(
        'email address',
        unique=False,
        error_messages={
            'unique': 'A user with that email already exists.'
        },
        blank=True
    )

    address = models.CharField(max_length=50, blank=False, null=False)
    district = models.CharField(max_length=25, blank=False, null=False)
    reference = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return "Nombre:{}\nApellido:{}".format(self.first_name, self.last_name)

    class Meta(BlackMarketModel.Meta):
        ordering = ['-modified', '-created']
