from rest_framework import permissions


class RetrieveListPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and request.user.is_admin
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return all(
                (request.user.is_authenticated(),
                 (obj == request.user or request.user.is_admin)))
        else:
            return False
