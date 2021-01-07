"""Items admin. """

# Django
from django.contrib import admin

# Model
from .models.items import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Customer admin. """

    list_display = (
        'name',
        'category',
        'description',
        'type_item',
        'unit',
        'price',
        'owner',
        'is_active'
    )
    search_fields = ('first_name', 'last_name')
