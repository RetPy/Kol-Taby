from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.child.models import Child, Answer
from apps.child.serializers import ChildSerializer, AnswerSerializer


class ChildPagination(LimitOffsetPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ChildPagination


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'child', 'date']

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)
