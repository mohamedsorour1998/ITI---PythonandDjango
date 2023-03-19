from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.question_list, name='question_list'),
    # ex: /polls/5/
    path('<int:pk>/', views.question_detail, name='question_detail'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/create/
    path('create/', views.question_create, name='question_create'),
    # ex: /polls/delete/5/
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # ex: /polls/login/
    path('login/', views.Login_view, name='login'),
    # ex: /polls/logout/
    path('logout/', views.Logout_view, name='logout'),
    # ex: /polls/signup/
    path('signup/', views.Signup_view, name='signup'),
]
