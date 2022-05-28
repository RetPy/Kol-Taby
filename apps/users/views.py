from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets

from apps.users.serializers import *
from apps.users.permissions import IsAdmin, IsOwner


class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD для Админа
    """
    queryset = User.objects.filter(is_staff=False)
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


class CurrentUser(GenericAPIView):
    serializer_class = CurrentUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CurrentUserSerializer(data=self.request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            try:
                access_token = AccessToken(token)
                user = User.objects.get(id=access_token['user_id'])
                return Response({
                    'id': user.id,
                    'alias': user.alias,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'patronymic': user.patronymic,
                    'birthday': user.birthday,
                    'phone_number': user.phone_number,
                    'email': user.email,
                    'status': 1 if user.is_superuser else 2
                })
            except Exception as ex:
                return Response({'error': f'{ex}'})
