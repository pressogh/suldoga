from django.urls import path
from django.conf.urls.static import static

from suldoga import settings
from . import views


app_name = 'board'

urlpatterns = [
    path('board', views.BoardView, name='board'),
    path('regist/', views.regist, name='create'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
]
