from rest_framework import permissions


# restrict users from modifying comments they did not create,
# we can add a custom permission class to the CommentViewSet
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
