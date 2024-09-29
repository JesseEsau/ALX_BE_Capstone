from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission only allow oners of an object to edit or delete it."""

    def has_object_permission(self, request, view, obj):
        #read-only permissions are allowed for any request.

        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions to only owners of the object
        return obj.organizer == request.user