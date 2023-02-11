from rest_framework import permissions


class IsInstructor(permissions.BasePermission):
    """clarify that the requested user is instructor"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.user_type.id == 1
