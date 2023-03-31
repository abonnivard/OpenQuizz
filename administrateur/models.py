from django.db import models
import uuid

#Les valeurs par défaut seront null
class Question(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pseudo = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255, default='null')
    reponse2 = models.CharField(max_length=255, default='null')
    reponse3 = models.CharField(max_length=255, default='null')
    reponse4 = models.CharField(max_length=255, default='null')
    reponseVrai = models.CharField(max_length=255, default='null') #Si qcm
    reponse = models.CharField(max_length=255, default='null') #Si pas qcm
    qcm = models.BooleanField(default=False)
    numero = models.IntegerField(default=0) #ne sert à rien d 'autre que la simplification du processus de suppression de questions



#Liste de l'ensembles des thémes créés
class Theme(models.Model):
    nom = models.CharField(max_length=255)



class Quizz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pseudo = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="null")
    questions = models.TextField(default="")
    mode = models.CharField(max_length=255)
    timer = models.IntegerField(default=0)
    afficher = models.BooleanField(default=False)
    stocker = models.BooleanField(default=False)
    numero = models.IntegerField(default=0)  # ne sert à rien d 'autre que la simplification du processus de suppression de questions

