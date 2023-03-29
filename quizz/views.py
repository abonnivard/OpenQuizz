from django.shortcuts import render
from administrateur.models import Quizz, Question
import time


i=0
def interfaceUser(request):

    if request.method == 'GET':

        # Si qcm

        start = time.perf_counter()
        global i
        question=Question.objects.all()

        longueur=len(question)
        nbrPage=longueur/4 ##on suppose qu'il y a 4*i questions
        end= time.perf_counter()
        while start-end < 10: #Quizz.timer ici juste 10s pour repondre

            #context = {
            #    "questions" : question[4*i:4*(i+1)]
            #}
            context = {
                "question" : question[i].enonce
            }

            i+=1
            end=time.perf_counter()
            render(context)

            i=0
    return render(request, 'quizz/interfaceUser.html')






















def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')
def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')

def waitingpageUser(request):
    return render(request, 'quizz/waitingpageUser.html')