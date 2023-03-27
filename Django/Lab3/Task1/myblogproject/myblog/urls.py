from . import views
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, PostListWithFilterAndSearch, CommentListWithFilterAndSearch
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('api/post', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('api/post/<int:pk>',
         PostViewSet.as_view({
             'put': 'update',
             'delete': 'destroy'
         })),
    path('api/comment',
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create',
         })),
    path('api/comment/<int:pk>',
         CommentViewSet.as_view({
             'put': 'update',
             'delete': 'destroy'
         })),
    path('api/postfilter/',
         PostListWithFilterAndSearch.as_view(),
         name='postfilter'),
    path('api/commentfilter/',
         CommentListWithFilterAndSearch.as_view(),
         name='commentfilter'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
]
