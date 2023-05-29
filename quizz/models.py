from django.db import models
from administrateur.models import Quizz

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=255)
    id_quizz = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    question = models.CharField(max_length=255,default='')

##créer une autre base répertoriant pour chaque question, l'ensemble des reponses des users pour ensuite les afficher