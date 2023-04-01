from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question
from quizz.models import User
import time

@csrf_protect
def interfaceUser(request,id):
    i=0
    quizz = Quizz.objects.all().filter(id=id)[0]
    questions_id=quizz.questions
    list_id=questions_id.split(',') #ne pas prendre le dernier element (juste ' ')
    timer =quizz.timer
    start = time.perf_counter()
    end=time.perf_counter()
    while i<len(list_id): #ne marche pas puisque pas une liste, il faut compter le nombre de virgule
        question=Question.objects.get(id=list_id[i])
        print(question)
        context = {
            "question": question.enonce,
            'timer': timer
        }
        while abs(start-end)<timer:
            end=time.perf_counter()

        i+=1

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
