"""Category model. """

# Django
from django.db import models

# Utilities
from App.utils.models import BlackMarketModel


class Category(BlackMarketModel):
    """Category model. 
    It's a item category """

    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)
