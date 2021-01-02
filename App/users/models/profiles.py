"""Profile model. """

# Django
from django.db import models

# Utilities
from App.utils.models import BlackMarketModel


class Profile(BlackMarketModel):
    """A profile holds a user's public like biography, picture,
    and statistics. """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='user/picture',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=150, blank=True)

    # stats

    def __str__(self):
        """Return user's str. representation."""
        return str(self.user)
