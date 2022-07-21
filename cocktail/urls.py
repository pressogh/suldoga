from django.urls import path
from . import views

app_name = 'cocktail'
urlpatterns = [
    path('', views.MainView, name='main')
]
