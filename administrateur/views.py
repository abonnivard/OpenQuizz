from django.shortcuts import render
from .models import Question
from django.contrib.auth.models import User

def dashboard(request):
    print(request.user.username)
    Questions = Question.objects.all()
    print(Questions)
    context = {
        "questions":Questions
    }
    return render(request, "administrateur/dashboard.html", context)