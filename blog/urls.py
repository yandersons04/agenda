from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('per', views.per, name='per'),
    path('per_list', views.per_list, name='per_list'),
    path('per_new', views.per_new, name='per_new'),
    path('per/<pergunta>/', views.per_detail, name='per_detail'),
    path('per/<pergunta>/edit/', views.per_edit, name='per_edit'),
]