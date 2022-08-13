from django.urls import path
from django.conf.urls.static import static

from suldoga import settings
from . import views


app_name = 'cocktail'
urlpatterns = [
    path('', views.MainView, name='main'),
    path('info', views.InfoView, name='info'),
    path('modal', views.ModalView, name='modal'),
    path('cocktail', views.ListView, name='cocktail'),
    path('kocktail', views.KListView, name='kocktail'),
    path('test', views.TestView, name='test'),
]
