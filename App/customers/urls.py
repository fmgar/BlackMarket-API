"""Customers URLs. """

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .views.customers import CustomersViewSet

router = DefaultRouter()
router.register(r'customers', CustomersViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls))
]
