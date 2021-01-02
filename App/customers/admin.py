"""Customers admin. """

# Django
from django.contrib import admin

# Model
from App.customers.models.customers import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin. """

    list_display = (
        'first_name',
        'last_name',
        'identification',
        'phone'
    )
    search_fields = ('first_name', 'last_name')
