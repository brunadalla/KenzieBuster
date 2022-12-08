from rest_framework import permissions
from users.models import User


class IsTheUserOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.user.is_employee:
            return True

        return user.email == request.user.email
