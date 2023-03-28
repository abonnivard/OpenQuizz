from django.contrib import admin
from django.urls import path
from .views import dashboard, suppression, creation_de_quizz, enregistrement, banquequestions, suppression_question

app_name = 'administrateur'

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('suppression/', suppression, name="suppression"),
    path('creation-quizz/',creation_de_quizz, name='creation_de_quizz' ),
    path('enregistrement/', enregistrement, name="enregistrement"),
    path('banque-question/', banquequestions, name="banquequestions"),
    path('suppression-question/', suppression_question, name="suppression_question"),
]
