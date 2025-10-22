from rest_framework import permissions

class CheckStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return obj.status_movie == 'simple'
        if request.user.status == 'simple' and obj.status_movie == 'simple':
            return True
        elif request.user.status == 'Diamond':
            return True

        return False
