from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.todos.models import Todo
from apps.todos.serializers import TodoSerializer

from utils.permissions import IsAdmin, IsAuthenticated, IsOwner


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'created_date', 'deadline', 'status']
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'create': [IsAdmin],
        'retrieve': [IsAdmin | IsOwner],
        'update': [IsAdmin | IsOwner],
        'delete': [IsAdmin],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


@api_view(['GET'])
def get_user_todos(request, pk):
    try:
        childs = Todo.objects.filter(employee=pk)
        serializer = TodoSerializer(childs, many=True)
        return Response(serializer.data)
    except:
        return Response([])
