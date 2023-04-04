from django.contrib import admin
from .models import Question, Quizz
from quizz.models import User

admin.site.register(Question)
admin.site.register(Quizz)
admin.site.register(User)

