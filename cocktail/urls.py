from django.urls import path
from . import views

app_name = 'cocktail'

urlpatterns = [
    path('', views.MainView, name='main'),
    path('info', views.InfoView, name='info'),
    path('cocktail', views.ListView, name='cocktail'),
    path('kocktail', views.KListView, name='kocktail'),
    path('test', views.TestView, name='test'),
]
