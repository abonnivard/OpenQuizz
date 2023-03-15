from django.db import models


#Les valeurs par défaut seront null
class Question(models.Model):
    pseudo = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255)
    reponse2 = models.CharField(max_length=255)
    reponse3 = models.CharField(max_length=255)
    reponce4 = models.CharField(max_length=255)
    reponseVrai = models.CharField(max_length=255) #Si qcm
    reponse = models.CharField(max_length=255) #Si pas qcm
    qcm = models.BooleanField(default=False)
