from django.urls import path
from django.conf.urls.static import static

from suldoga import settings
from . import views


app_name = 'cocktail'
urlpatterns = [
    path('', views.MainView, name='main'),
    path('info', views.InfoView, name='info'),
    path('modal', views.ModalView, name='modal'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
