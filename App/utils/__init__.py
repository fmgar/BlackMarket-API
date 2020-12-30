"""Django.models utilities."""

# Django
from django.db import models


class BlackMarketModel(models.Model):
    """BlackMarket base model.

    BlackMarketModel acts as an abstract base class from which every
    other model in the project will inherit."""

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'created at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
