from django.contrib import admin
from django.urls import path
from .views import interfaceProf, interfaceUser

app_name = 'quizz'

urlpatterns = [
    path('interfaceProf/', interfaceProf, name='interfaceProf'),
    path('interfaceUser/', interfaceUser, name='interfaceUser'),
]
