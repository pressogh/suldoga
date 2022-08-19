from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from suldoga import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cocktail.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
