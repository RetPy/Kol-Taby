from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.permissions import IsAdmin


class UserViewSet(ModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializer
