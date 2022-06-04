from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.child.models import Child, Answer
from apps.users.models import User
from apps.child.serializers import ChildSerializer, AnswerSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'child', 'date']

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


@api_view(['GET'])
def get_user_child(request, pk):
    try:
        childs = Child.objects.filter(employee=pk)
        serializer = ChildSerializer(childs, many=True)
        return Response(serializer.data)
    except:
        return Response([])
