from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.permissions import IsAdmin, IsOwner


class UserViewSet(ModelViewSet):
    """
    CRUD для Админа
    """
    queryset = User.objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ['retrieve']:
            self.permission_classes = [IsAdmin() | IsOwner()]
            return self.permission_classes
        self.permission_classes = [IsAdmin()]
        return self.permission_classes
