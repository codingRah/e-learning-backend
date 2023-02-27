from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    """clarify that the requested user is  a superuser"""

    def has_permission(self, request, view):
        return request.user.is_superuser == True