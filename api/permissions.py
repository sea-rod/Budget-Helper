from rest_framework import permissions


class UserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
