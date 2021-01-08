"""Users views. """

# Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action


# Serializers
from App.users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer, AccountVerificationSerializer


class UserViewSet(viewsets.GenericViewSet):
    """User view set. 

    Handle login, sign up, and verification.
    """

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login up."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """User verification"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now you can use BlackMarket!!'}

        return Response(data, status=status.HTTP_200_OK)
