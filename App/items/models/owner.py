"""Owner model. """

# Django
from django.db import models

# Utilities
from App.utils.models import BlackMarketModel


class Owner(BlackMarketModel):
    """It's a owner item. """

    name = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)
