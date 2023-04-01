from django.contrib import admin
from django.urls import path
from .views import interfaceProf, interfaceUser, waitingpageProf, waitingpageUser0,waitingpageUser1

app_name = 'quizz'

urlpatterns = [
    path('interfaceProf/', interfaceProf, name='interfaceProf'),
    path('interfaceUser/id=<str:id>', interfaceUser, name="modifyquizz"),
    path('waitingpageProf/', waitingpageProf, name='waitingpageProf'),
    path('waitingpageUser0/', waitingpageUser0, name="waitingpageUser0"),
    path('waitingpageUser1/', waitingpageUser1, name="waitingpageUser1"),
]
