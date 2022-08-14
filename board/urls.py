from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.ListView, name='main'),
    path('create', views.CreateView, name='create'),
    path('detail/<int:post_id>', views.DetailView, name='detail'),
]
