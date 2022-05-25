from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apps.child.models import Child, Answer
from apps.child.serializers import ChildSerializer, AnswerSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child.objects
    serializer_class = ChildSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'child', 'date']
