from django.urls import path
from . import views

app_name = 'cocktail'

urlpatterns = [
    path('', views.MainView, name='main'),
    path('info', views.InfoView, name='info'),
    path('cocktail', views.ListView, name='cocktail'),
    path('kocktail', views.KListView, name='kocktail'),
    path('combination2', views.Combination2View, name="combination2"),
    path('test', views.TestView, name='test'),
    path('like/<int:cocktails_id>', views.LikeView, name="likes"),
    path('myprofile', views.myprofile, name='profile'),
]
