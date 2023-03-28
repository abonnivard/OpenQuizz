from django.shortcuts import render, redirect
from .models import Question, Quizz
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json as json

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
    quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
    for k in range(len(quizzs)):
        quizzs[k].numero = k
        quizzs[k].save()

    context = {
        "quizzs":quizzs,
    }
    return render(request, "administrateur/dashboard.html", context)


#reste à rendre required au moins deux du qcm et la réponse selon le mode


def suppression(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        quizzsupp = Quizz.objects.all().filter(pseudo=str(request.user.username)).filter(numero=numero)
        quizzsupp.delete()
        return redirect("/dashboard/")

    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()
        quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
        for k in range(len(quizzs)):
            quizzs[k].numero = k
            quizzs[k].save()

        context = {
            "questions": questions,
            "quizzs": quizzs,
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
        time = request.POST.get('timer')

        classementdisplay =request.POST.get('classementdisplay')
        if classementdisplay=="true":
            classementdisplay = True
        else:
            classementdisplay = False

        stocker = request.POST.get('stocker')
        if stocker=="true":
            stocker = True
        else:
            stocker = False

        mode = request.POST.get('mode')
        name = request.POST.get('name')
        liste_questions = []
        print(stocker, classementdisplay)
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for question in questions:
            if str(question.numero) in liste:
                print(question.numero, 'ok')
                liste_questions.append(question)
        newQuizz = Quizz(pseudo=str(request.user.username),name=name, mode=mode, afficher=classementdisplay, timer=time, stocker=stocker)
        newQuizz.save()
        return redirect("/dashboard/")
    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()
        quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
        for k in range(len(quizzs)):
            quizzs[k].numero = k
            quizzs[k].save()

        context = {
            "questions": questions,
            "quizzs": quizzs,
        }
        return render(request, "administrateur/dashboard.html", context)



def banquequestions(request):
    if request.method == 'POST':
        checkbox = request.POST.getlist('choice')
        enonce = request.POST.get('enonce')
        if 'qcm' in checkbox:
            choix1 = request.POST.get('choix1')
            choix2 = request.POST.get('choix2')
            choix3 = request.POST.get('choix3')
            choix4 = request.POST.get('choix4')
            reponseqcm = request.POST.get('reponseqcm')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse1=choix1, reponse2=choix2,
                                   reponse3=choix3, reponse4=choix4, reponseVrai=reponseqcm, qcm=True)
            newquestion.save()
        else:
            reponselongue = request.POST.get('reponselongue')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse=reponselongue)
            newquestion.save()

        return redirect('/banque-question/')
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()

    context = {
        "questions": questions,
    }
    return render(request, 'administrateur/banquequestions.html', context)


def suppression_question(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        questionsupp = Question.objects.all().filter(pseudo=str(request.user.username)).filter(numero=numero)
        questionsupp.delete()
        return redirect("/banque-question/")

    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()()

        context = {
            "questions": questions,
        }
        return render(request, "administrateur/banquequestions.html", context)
