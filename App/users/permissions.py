"""User permissions. """

# Django REST framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow acces only to objects owned by the requesting user. """

    message = 'No tienes permiso para acceder acceder a este recurso'

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same. """
        return request.user == obj
