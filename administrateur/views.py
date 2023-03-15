from django.shortcuts import render
from .models import Question
from django.contrib.auth.models import User

def dashboard(request):
    Questions = Question.objects.all().filter(pseudo=str(request.user.username))
    context = {
        "questions":Questions
    }
    return render(request, "administrateur/dashboard.html", context)