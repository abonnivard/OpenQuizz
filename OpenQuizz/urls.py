from django.contrib import admin
from django.urls import path, include
from .views import index, erreurId
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('erreurId/', erreurId, name="erreurId"),
    path('', include('administrateur.urls')),
    path('', include('utilisateur.urls')),
    path('', include('quizz.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
