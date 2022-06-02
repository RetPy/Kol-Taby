from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import *
from apps.child.views import *
from apps.todos.views import *

router = DefaultRouter()
router.register(
    'users',
    UserViewSet,
    basename='users',
)
router.register(
    'child',
    ChildViewSet,
    basename='child',
)
router.register(
    'answer',
    AnswerViewSet,
    basename='answer',
)
router.register(
    'todo',
    TodoViewSet,
    basename='todo'
)

urlpatterns = router.urls
urlpatterns += [
    path('users/<int:pk>/change_password/', UserChangePasswordView.as_view()),
    path('current-user/', CurrentUser.as_view()),
    path('check-alias/', CheckAliasAPIView.as_view()),
]
