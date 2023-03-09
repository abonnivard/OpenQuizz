from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('administrateur.urls')),
    path('', include('utilisateur.urls')),
    path('', include('quizz.urls')),
]
