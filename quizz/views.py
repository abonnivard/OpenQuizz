from django.shortcuts import render
from administrateur.models import Quizz, Question
from quizz.models import User
import time


i=0
def interfaceUser(request):

    ping= str(request.user.username)
    #timer =
        # Si qcm

    #    start = time.perf_counter()
    #    global i
    #    question=Question.objects.all()
    #    longueur=len(question)
    #    nbrPage=longueur/4 ##on suppose qu'il y a 4*i questions = qcm
     #    end= time.perf_counter()


    return render(request, 'quizz/interfaceUser.html')





















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
