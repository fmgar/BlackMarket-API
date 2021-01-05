"""Users views. """

# Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from App.users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer, AccountVerificationSerializer


class UserLoginAPIView(APIView):
    """User login API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP post request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User sign up API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP post request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)


class AccountVerificationAPIView(APIView):
    """Account verification API view"""

    def post(self, request, *args, **kwargs):
        """Handle HTTP post request."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now you can use BlackMarket!!'}

        return Response(data, status=status.HTTP_200_OK)
