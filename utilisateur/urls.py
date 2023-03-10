from django.contrib import admin
from django.urls import path
from .views import waitingpage

app_name = 'utilisateur'

urlpatterns = [
    path('rejoindre/', waitingpage, name="waitingpage"),
]
