from django.db import models


#Les valeurs par défaut seront null
class Question(models.Model):
    pseudo = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255, default='null')
    reponse2 = models.CharField(max_length=255, default='null')
    reponse3 = models.CharField(max_length=255, default='null')
    reponse4 = models.CharField(max_length=255, default='null')
    reponseVrai = models.CharField(max_length=255, default='null') #Si qcm
    reponse = models.CharField(max_length=255, default='null') #Si pas qcm
    qcm = models.BooleanField(default=False)
