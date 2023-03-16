from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth.models import User


def dashboard(request):
    if request.method == 'POST':
        checkbox = request.POST.getlist('choice')
        enonce = request.POST.get('enonce')
        if 'qcm' in checkbox:
            choix1 = request.POST.get('choix1')
            choix2 = request.POST.get('choix2')
            choix3 = request.POST.get('choix3')
            choix4 = request.POST.get('choix4')
            reponseqcm = request.POST.get('reponseqcm')
            newquestion = Question(pseudo=str(request.user.username) ,enonce=enonce, reponse1=choix1, reponse2=choix2, reponse3=choix3, reponse4=choix4, reponseVrai=reponseqcm, qcm=True)
            newquestion.save()
        reponselongue = request.POST.get('reponselongue')
        newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse=reponselongue)
        newquestion.save()
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        context = {
            "questions": questions
        }
        return render(request, "administrateur/dashboard.html", context)

    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    context = {
        "questions": questions
    }
    return render(request, "administrateur/dashboard.html", context)
