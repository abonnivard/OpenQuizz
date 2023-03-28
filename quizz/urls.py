from django.contrib import admin
from django.urls import path
from .views import interfaceProf, interfaceUser, waitingpageProf, waitingpageUser

app_name = 'quizz'

urlpatterns = [
    path('interfaceProf/', interfaceProf, name='interfaceProf'),
    path('interfaceUser/', interfaceUser, name='interfaceUser'),
    path('waitingpageProf/', waitingpageProf, name='waitingpageProf'),
    path('waitingpageUser/', waitingpageUser, name="waitingpageUser"),
]
