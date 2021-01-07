"""Items URLs. """

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .views.items import ItemsViewSet
from .views.category import CategoryViewSet
from .views.unit import UnitViewSet
from .views.owner import OwnerViewSet

router = DefaultRouter()

router.register(r'items', ItemsViewSet, basename='items')
router.register(r'categorys', CategoryViewSet, basename='categorys')
router.register(r'units', UnitViewSet, basename='units')
router.register(r'owners', OwnerViewSet, basename='owners')

urlpatterns = [
    path('', include(router.urls))
]
