from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from utils.permissions import IsAuthenticated, IsAdmin
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.child.models import Child, Answer
from apps.child.serializers import ChildSerializer, AnswerSerializer, UserAnswerSerializer


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


class AnswerLastListView(ListAPIView):
    queryset = Answer.objects.all().order_by('-id')[:5]
    serializer_class = AnswerSerializer
    permission_classes = [IsAdmin]


class AnswerCreateAPIView(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        child = Child.objects.get(pk=self.kwargs.get('pk'))
        serializer.save(
            employee=self.request.user,
            child=child,
        )


@api_view(['GET'])
def get_user_child(request, pk):
    paginator = LimitOffsetPagination()
    paginator.page_size = 1000000
    try:
        children = Child.objects.filter(employee=pk)
        result = paginator.paginate_queryset(children, request)
        serializer = ChildSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    except:
        return paginator.get_paginated_response([])


@api_view(['GET'])
def get_user_answers(request, pk):
    paginator = LimitOffsetPagination()
    paginator.page_size = 1000000
    try:
        answers = Answer.objects.filter(employee=pk)
        result = paginator.paginate_queryset(answers, request)
        serializer = UserAnswerSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    except:
        return paginator.get_paginated_response([])


@api_view(['GET'])
def get_user_last_answers(request, pk):
    paginator = LimitOffsetPagination()
    paginator.page_size = 1000000
    try:
        last_five_answers = Answer.objects.filter(employee=pk).order_by('-id')[:5]
        result = paginator.paginate_queryset(last_five_answers, request)
        serializer = UserAnswerSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    except:
        return paginator.get_paginated_response([])
