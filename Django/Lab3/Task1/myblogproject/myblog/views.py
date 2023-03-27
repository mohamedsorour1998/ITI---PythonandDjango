from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Post, Comment
from myblog.serializers import PostSerializer, CommentSerializer
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics


class PostViewSet(ViewSet):
    """
    This is the viewset for the Post model and it have the following methods:
    1- list: to get all the posts
    2- create: to create a new post
    3- update: to update a post
    4- destroy: to delete a post
    """
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response('Post deleted')


class CommentViewSet(ViewSet):
    """
    This is the viewset for the Comment model and it have the following methods:
    1- list: to get all the comments
    2- create: to create a new comment
    3- update: to update a comment
    4- destroy: to delete a comment
    """
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        # Add authorization to the Comment viewset so that
        # users can only modify comments they have created.
        if self.request.user.is_authenticated:
            pk = kwargs.get('pk')
            try:
                comment = Comment.objects.filter(owner=self.request.user).get(
                    pk=pk)
            except Comment.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = CommentSerializer(
                comment,
                data=request.data,
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response('Comment deleted')


class PostListWithFilterAndSearch(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentListWithFilterAndSearch(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['body']
    search_fields = ['body']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer