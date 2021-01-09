"""Users views. """

# Django REST framework
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,

)
from ..permissions import IsAccountOwner

# Serializers
from App.users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer, AccountVerificationSerializer, ProfileModelSerializer

# Models
from ..models.users import User


class UserViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    """User view set. 

    Handle login, sign up, and verification.
    """
    queryset = User.objects.all()  # We could use filter
    serializer_class = UserModelSerializer
    lookup_field = 'username'  # Change in url id for username

    def get_permissions(self):
        """Assign permissions based on action. """
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

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

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)
