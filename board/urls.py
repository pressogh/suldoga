from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('', views.ListView, name='board'),
    path('regist/', views.PostCreateView, name='create'),
    path('detail/<int:post_id>/', views.DetailView, name='detail'),
]
