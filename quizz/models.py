from django.db import models

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=255)
    id_quizz = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    onGame= models.BooleanField()
