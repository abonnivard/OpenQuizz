from django.contrib import admin
from django.urls import path
from .views import interfaceProf, interfaceUser, waitingpageProf, waitingpageUser0,waitingpageUser1, finQuizz, userAnswered

app_name = 'quizz'

urlpatterns = [
    path('interfaceProf/', interfaceProf, name='interfaceProf'),
    path('interfaceUser/id=<str:id_quizz>/num_question=<str:num_question>', interfaceUser, name="interfaceUser"),
    path('waitingpageProf/', waitingpageProf, name='waitingpageProf'),
    path('waitingpageUser0/', waitingpageUser0, name="waitingpageUser0"),
    path('waitingpageUser1/', waitingpageUser1, name="waitingpageUser1"),
    path('finQuizz/', finQuizz, name="finquizz"),
    path('userAnswered/', userAnswered, name="userAnswered"),

]
