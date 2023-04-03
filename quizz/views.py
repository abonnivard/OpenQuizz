from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question
from quizz.models import User
import time

@csrf_protect
def interfaceUser(request,pseudo, id_quizz, num_question):
    quizz = Quizz.objects.all().filter(id=id_quizz)[0]
    questions_id = quizz.questions
    list_id = questions_id.split(',') #ne pas prendre le dernier element (juste ' ')
    l=len(list_id)-1
    if (int(num_question)==l):
        return HttpResponseRedirect('/finQuizz/'+pseudo+"/id="+id_quizz)
    else:
        timer =quizz.timer
        question=Question.objects.get(id=list_id[int(num_question)].strip()) ##strip pour enlever tous les espaces gênants
        context = {
            "pseudo" : pseudo,
            "image" : str(question.image),
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

def waitingpageUser0(request,id): #on rentre son pseudo apres avoir rentrer l'id du quizz
    users=User.objects.all().filter(id_quizz=id) ##on prend que du meme quizz ==> a la fin de chaque quizz on supprime les user du quizz !
    pseudo = request.POST.get('pseudo')
    context = {
        'url': "http://127.0.0.1:8000/waintingUser1/" + "pseudo=" + str(pseudo) + "/id=" + id
    }
    if request.method == 'POST':
        for user in users: #pseudo déjà existant ?
            if pseudo == user.pseudo:
                return HttpResponseRedirect('erreurPseudo/')  # voir pour afficher le message d'erreur dans la page
        newUser = User(pseudo=pseudo, id_quizz=id, score=0)
        newUser.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/waitingpageUser1/"+pseudo+"/id="+str(id))
    return render(request, 'quizz/waitingpageUser0.html',context)

def waitingpageUser1(request,pseudo,id): #on arrive dans le lobby avc tous les joueurs on peut par exemple custom les designs des persos
    context = {
                 'url': "http://127.0.0.1:8000/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id + "/num_question=0"
    }

    if request.method == 'POST':
        return HttpResponseRedirect("http://127.0.0.1:8000/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id + "/num_question=0")
    return render(request, 'quizz/waitingpageUser1.html',context)

def finQuizz(request,id,pseudo):
    User.objects.all().get(id_quizz=id,pseudo=pseudo).delete()
    return render(request, 'quizz/finquizz.html')

def userAnswered(request):
    return render(request, 'quizz/userAnswered.html')