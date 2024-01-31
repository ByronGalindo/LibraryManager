from rest_framework import permissions
from .models import CustomUser

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == CustomUser.ADMIN or request.user.is_superuser)

class IsLibrarianOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == CustomUser.ADMIN or request.user.is_superuser or  request.user.user_type == CustomUser.LIBRARIAN)

class IsClientOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == CustomUser.ADMIN or request.user.is_superuser or request.user.user_type == CustomUser.CLIENT)

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user.user_type == CustomUser.ADMIN or request.user.is_superuser or obj.pk == request.user.pk)
