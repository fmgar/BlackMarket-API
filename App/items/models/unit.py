"""Unit model. """

# Django
from django.db import models

# Utilities
from App.utils.models import BlackMarketModel


class Unit(BlackMarketModel):
    """It's a unit for item. """

    name = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)
