from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet
from apps.child.views import ChildViewSet, AnswerViewSet

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

urlpatterns = router.urls
