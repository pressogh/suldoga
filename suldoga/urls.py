from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from suldoga import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cocktail.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('board.urls')),
]
