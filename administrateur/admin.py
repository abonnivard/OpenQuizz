from django.contrib import admin
from .models import Question, Theme, Quizz

admin.site.register(Question)
admin.site.register(Theme)
admin.site.register(Quizz)

