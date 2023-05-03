from django.contrib import admin
from django.urls import path
from .views import interfaceProf0,interfaceProf1, resultat, interfaceUser, waitingpageProf, waitingpageUser0,waitingpageUser1, finQuizz,finQuizzProf, userAnswered,erreurPseudo,userAnswered_resultat

app_name = 'quizz'

urlpatterns = [
    path('interfaceProf0/id=<str:id>/', interfaceProf0, name='interfaceProf0'),
    path('interfaceProf1/id=<str:id>/num_question=<str:num_question>', interfaceProf1, name='interfaceProf1'),
    path('interfaceUser/<str:pseudo>/id=<str:id_quizz>/num_question=<str:num_question>', interfaceUser, name="interfaceUser"),
    path('waitingpageProf/', waitingpageProf, name='waitingpageProf'),
    path('waitingpageUser0/id=<str:id>/<str:error>/', waitingpageUser0, name="waitingpageUser0"),
    path('waitingpageUser1/<str:pseudo>/id=<str:id>/', waitingpageUser1, name="waitingpageUser1"),
    path('finQuizz/<str:pseudo>/id=<str:id>/', finQuizz, name="finquizz"),
    path('finQuizzProf/id=<str:id>/', finQuizzProf, name="finQuizzProf"),
    path('interfaceUser/<str:pseudo>/id=<str:id_quizz>/num_question=<str:num_question>/userAnswered/<str:question_answered>', userAnswered, name="userAnswered"),
    path('interfaceUser/<str:pseudo>/id=<str:id_quizz>/num_question=<str:num_question>/userAnswered/<str:question_answered>/resultat', userAnswered_resultat, name="userAnswered_resultat"),
    path('interfaceProf1/id=<str:id>/num_question=<str:num_question>/resultat', resultat, name="resultat"),

]
