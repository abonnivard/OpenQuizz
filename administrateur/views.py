from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
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
        else:
            reponselongue = request.POST.get('reponselongue')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse=reponselongue)
            newquestion.save()

        return redirect('/dashboard/')
    print('ok')
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()
    context = {
        "questions": questions
    }
    return render(request, "administrateur/dashboard.html", context)


#reste à rendre required au moins deux du qcm et la réponse selon le mode


def suppression(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        questionsupp = Question.objects.all().filter(pseudo=str(request.user.username)).filter(numero=numero)
        questionsupp.delete()
        return redirect("/suppression/")

    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()
        context = {
            "questions": questions
        }
        return render(request, "administrateur/dashboard.html", context)



def creation_de_quizz(request):
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()
    context = {
        "questions": questions
    }
    return render(request, "administrateur/creationQuizz.html", context)

def enregistrement(request):
    if request.method == 'POST':
        liste = request.POST.get('liste')
        print(liste)
