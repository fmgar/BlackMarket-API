"""Items model. """

# Django
from django.db import models

# Utilities
from App.utils.models import BlackMarketModel

# Models
from .category import Category
from .unit import Unit
from .owner import Owner


class Item(BlackMarketModel):
    """Items model. 
    Is a model to items we goin to sell """

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200, blank=True)
    type_item = models.CharField(max_length=15, blank=True)
    unit = models.ForeignKey(Unit, blank=True, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    owner = models.ForeignKey(Owner, blank=True, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'name:{}'.format(self.name)
