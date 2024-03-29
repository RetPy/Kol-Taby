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
    'administration',
    AdminViewSet,
    'administration'
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
    path('administration/<int:pk>/change_password/', AdminChangePasswordView.as_view()),
    path('users/<int:pk>/change_password/', UserChangePasswordView.as_view()),
    path('users/<int:pk>/children/', get_user_child),
    path('users/<int:pk>/answers/', get_user_answers),
    path('users/<int:pk>/answers/last/', get_user_last_answers),
    path('users/<int:pk>/todo/', get_user_todos),
    path('users/<int:pk>/todo/last/', get_user_last_todos),
    path('child/<int:pk>/create_answer/', AnswerCreateAPIView.as_view()),
    path('answers/last/', AnswerLastListView.as_view()),
    path('current-user/', CurrentUser.as_view()),
    path('check-alias/', CheckAliasAPIView.as_view()),
]
