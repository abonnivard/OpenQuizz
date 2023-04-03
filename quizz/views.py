from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question
from quizz.models import User
import time

@csrf_protect
def interfaceUser(request, id_quizz, num_question):
    quizz = Quizz.objects.all().filter(id=id_quizz)[0]
    questions_id = quizz.questions
    list_id = questions_id.split(',') #ne pas prendre le dernier element (juste ' ')
    l=len(list_id)-1
    if (int(num_question)==l):
        return HttpResponseRedirect('/finQuizz/')
    else:
        timer =quizz.timer
        question=Question.objects.get(id=list_id[int(num_question)].strip()) ##strip pour enlever tous les espaces gênants

        context = {
            "question": question.enonce,
            'timer': timer,
            'num_question': int(num_question.split()[0]), #seul moyen de convertire en int
            'id_quizz': id_quizz.strip(),
            'reponse1': question.reponse1,
            'reponse2': question.reponse2,
            'reponse3': question.reponse3,
            'reponse4': question.reponse4,
        }

    return render(request, 'quizz/interfaceUser.html',context)

def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')
def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')

def waitingpageUser0(request): #on rentre son pseudo apres avoir rentrer l'id du quizz
    return render(request, 'quizz/waitingpageUser0.html')

def waitingpageUser1(request): #on arrive dans le lobby avc tous les joueurs on peut par exemple custom les designs des persos
    pseudo = request.POST.get('pseudo')
    newUser= User(pseudo=pseudo)
    return render(request, 'quizz/waitingpageUser1.html')

def finQuizz(request):
    return render(request, 'quizz/finquizz.html')

def userAnswered(request):
    return render(request, 'quizz/userAnswered.html')