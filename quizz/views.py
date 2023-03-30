from django.shortcuts import render
from administrateur.models import Quizz, Question
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

def waitingpageUser(request):
    return render(request, 'quizz/waitingpageUser.html')