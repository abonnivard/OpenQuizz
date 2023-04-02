from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question
from quizz.models import User
import time

@csrf_protect
def interfaceUser(request,id_quizz,num_question):
    quizz = Quizz.objects.all().filter(id=id_quizz)[0]
    questions_id=quizz.questions
    list_id=questions_id.split(',') #ne pas prendre le dernier element (juste ' ')
    l=len(list_id)-1
    if (num_question==l):
        return HttpResponseRedirect('/finQuizz/')
    else:
        timer =quizz.timer
        question=Question.objects.get(id=list_id[int(num_question)].strip()) ##strip pour enlever tous les espaces gênants
        context = {
            "question": question.enonce,
            'timer': timer,
            'num_question' :int(num_question.split()[0]), #seul moyen de convertire en int
            'id_quizz' : id_quizz.strip()
        }

    return render(request, 'quizz/interfaceUser.html',context)





def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')
def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')

def waitingpageUser0(request):
    return render(request, 'quizz/waitingpageUser0.html')

def waitingpageUser1(request):
    pseudo = request.POST.get('pseudo')
    newUser= User(pseudo=pseudo)
    return render(request, 'quizz/waitingpageUser1.html')


def finquizz(request):
    return render(request, 'quizz/finquizz.html')