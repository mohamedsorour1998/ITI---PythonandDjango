from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('writer/<int:writer_id>', views.writer_detail, name='writer_detail'),
    path('book/<int:pk>/', views.BookDetailView, name='book_detail'),
]
