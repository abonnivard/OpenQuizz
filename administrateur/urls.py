from django.contrib import admin
from django.urls import path
from .models import Quizz
import uuid
from .views import dashboard, suppression, creation_de_quizz, enregistrement, banquequestions, suppression_question, modifierquizz

app_name = 'administrateur'

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('suppression/', suppression, name="suppression"),
    path('creation-quizz/',creation_de_quizz, name='creation_de_quizz' ),
    path('enregistrement/', enregistrement, name="enregistrement"),
    path('banque-question/', banquequestions, name="banquequestions"),
    path('suppression-question/', suppression_question, name="suppression_question"),
    path('modify/<str:id>', modifierquizz, name="modifyquizz")
]
