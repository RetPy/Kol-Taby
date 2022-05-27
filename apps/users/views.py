from rest_framework.decorators import action
from rest_framework.response import Response
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
    permission_classes_by_action = {
        'list': [IsAdmin],
        'create': [IsAdmin],
        'retrieve': [IsAdmin | IsOwner],
        'update': [IsAdmin],
        'delete': [IsAdmin],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
