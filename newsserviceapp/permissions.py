from rest_framework import permissions


class IsOwnerOrIsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        return bool(obj.author == request.user or request.user.is_staff)


class IsOwnerOrIsAdminForNews(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        return bool(obj.news.author == request.user or request.user.is_staff)