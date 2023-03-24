from rest_framework import viewsets, viewsets, versioning
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework.filters import SearchFilter


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # we add SearchFilter so users can search for posts
    # by adding a search query parameter to the URL, like this: /posts/?search=query.
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'content', 'date_published']
    search_fields = [
        'title',
    ]
    pagination_class = PageNumberPagination
    # Add support for versioning to the Post viewset so that future changes to the API
    # can be made without breaking existing clients
    versioning_class = versioning.NamespaceVersioning

    # a perform_create method that sets the author of the post to the current user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # IsAuthorOrReadOnly: users can only modify comments they created.
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]

    #  a get_queryset method that filters the comments by the post_pk parameter
    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post=post_id)


#  a perform_create method that sets the author of the comment to the current user
# before saving the comment to the database.

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
