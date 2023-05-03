from django.db import models
import uuid

#Les valeurs par défaut seront null
class Question(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pseudo = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, default='')
    intitule = models.CharField(max_length=255, default="")
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255, default='null')
    reponse2 = models.CharField(max_length=255, default='null')
    reponse3 = models.CharField(max_length=255, default='null')
    reponse4 = models.CharField(max_length=255, default='null')
    reponseVrai = models.CharField(max_length=255, default='null') #Si qcm
    reponse = models.CharField(max_length=255, default='null') #Si pas qcm
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    qcm = models.BooleanField(default=False)
    numero = models.IntegerField(default=0) #ne sert à rien d 'autre que la simplification du processus de suppression de questions




class Association(models.Model):
    idQuizz = models.UUIDField()
    idQuestion = models.UUIDField()

class Theme(models.Model):
    pseudo = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, default='')
    numero = models.IntegerField(default=0)


class Quizz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pseudo = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="null")
    mode = models.CharField(max_length=255)
    timer = models.IntegerField(default=0)
    afficher = models.BooleanField(default=False)
    stocker = models.BooleanField(default=False)
    numero = models.IntegerField(default=0)  # ne sert à rien d 'autre que la simplification du processus de suppression de questions
    onGame = models.CharField(max_length=10,default='0000000')

