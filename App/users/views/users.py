"""Users views. """

# Django REST framework
from rest_framework.views import APIView
from rest_framework import status

# Serializers
from App.users.serializers import UserLoginSerializer


class UserLoginAPIView(APIView):
    """User login API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP post request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        toke = serializer.save()
        data = {
            'status': 'ok',
            'token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)
