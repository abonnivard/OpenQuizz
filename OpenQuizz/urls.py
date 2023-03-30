from django.contrib import admin
from django.urls import path, include
from .views import index, erreurId

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('erreurId/', erreurId, name="erreurId"),
    path('', include('administrateur.urls')),
    path('', include('utilisateur.urls')),
    path('', include('quizz.urls')),
    path('', include('accounts.urls')),

]
