from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user:
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        if request.user:
            return request.user.is_superuser
        return False


class IsCurrentUser(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.id == request.user.id
        return False


class IsOwner(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.employee.id == request.user.id
        return False
