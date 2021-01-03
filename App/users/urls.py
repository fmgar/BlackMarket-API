"""Users URLs. """

# Django
from django.urls import path

# Views
from App.users.views import UserLoginAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
]
