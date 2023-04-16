from django.contrib import admin
from .models import Question, Quizz, Association, Theme
from quizz.models import User

admin.site.register(Question)
admin.site.register(Quizz)
admin.site.register(Association)
admin.site.register(User)
admin.site.register(Theme)

