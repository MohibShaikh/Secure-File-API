from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission that allows only the owner of a file or an admin to access it.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user.role == 'admin' or obj.owner == request.user)
