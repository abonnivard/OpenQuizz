from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question,Association
from quizz.models import User
import time

@csrf_protect
def interfaceUser(request,pseudo, id_quizz, num_question): #moyen d'afficher les questions dans le désordre ?

    if request.method=='GET':
        quizz = Association.objects.all().filter(idQuizz=id_quizz)
        questions_id = quizz[int(num_question)].idQuestion
        l=len(quizz)-1
        if (int(num_question)==l):
            return HttpResponseRedirect('/finQuizz/'+pseudo+"/id="+id_quizz)
        else:
            timer =Quizz.objects.all().get(id=id_quizz).timer
            question=Question.objects.get(id=questions_id) ##strip pour enlever tous les espaces gênants
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
    if request.method=='POST':
        quizz = Association.objects.all().filter(idQuizz=id_quizz)
        questions_id =  quizz[int(num_question)].idQuestion
        question = Question.objects.get(id=questions_id)#j'obtient la liste des questions
        reponseVrai=question.reponseVrai
        L=[request.POST.get('bouton1'),request.POST.get('bouton2'),request.POST.get('bouton3'),request.POST.get('bouton4')] #None="" si répondu, autre sinon
        j=L.index('') #jobtient le numero du bouton sur lequel l'user a appuyé
        player = User.objects.all().get(id_quizz=id_quizz,pseudo=pseudo[7:len(pseudo)]) #obliger de slicer pour obtenir le bo psuedo, pk?
        player.question+=str(j)+"/"
        if int(j) + 1 == int(reponseVrai):
            player.score += 1
            player.save()
            print("score modifié")
        return HttpResponseRedirect('num_question='+num_question+'/userAnswered/'+str(j))




def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')
def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')

def waitingpageUser0(request,id,error): #on rentre son pseudo apres avoir rentrer l'id du quizz
    users=User.objects.all().filter(id_quizz=id) ##on prend que du meme quizz ==> a la fin de chaque quizz on supprime les users du quizz !
    pseudo = request.POST.get('pseudo')
    if request.method == 'POST':
        for user in users: #pseudo déjà existant ?
            if pseudo == user.pseudo:
                return HttpResponseRedirect("/waitingpageUser0/id=" +str(id)+"/"+"error")
        newUser = User(pseudo=pseudo, id_quizz=id)
        newUser.save()
        return HttpResponseRedirect("/waitingpageUser1/"+pseudo+"/id="+str(id))
    if request.method=='GET':
        if str(error)=='error':
            context = {
                'erreur': False,
                'message_erreur': "Le pseudo est déjà pris par quelqu'un dans la game"
            }
            return render(request, 'quizz/waitingpageUser0Erreur.html',context)
        else:
            return render(request, 'quizz/waitingpageUser0.html')

def waitingpageUser1(request,pseudo,id): #on arrive dans le lobby avc tous les joueurs on peut par exemple custom les designs des persos, pour l'instant juste bouton valider
    context = {
                 'url': "/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id + "/num_question=0"
    }

    if request.method == 'POST':
        return HttpResponseRedirect("/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id + "/num_question=0")
        return HttpResponseRedirect("/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id + "/num_question=0")
    return render(request, 'quizz/waitingpageUser1.html',context)

def finQuizz(request,id,pseudo):
    context= {
        'score' : User.objects.all().get(id_quizz=id, pseudo=pseudo).score

    }
    print(User.objects.all().get(id_quizz=id,pseudo=pseudo))
    User.objects.all().get(id_quizz=id,pseudo=pseudo).delete()
    return render(request, 'quizz/finquizz.html')

def userAnswered(request,pseudo, id_quizz, num_question,question_answered):
    if request.method=='POST':
        return HttpResponseRedirect(str(question_answered)+'/resultat')
    return render(request, 'quizz/userAnswered.html')

def userAnswered_resultat(request,pseudo, id_quizz, num_question,question_answered):
    if request.method=='GET':

        for user in User.objects.all().filter(id_quizz=id_quizz): #pour faire comme kahoot en montrer la proportion des reponses des autres
            user.question+=str(question_answered)
            user.question.split("/") # j'obtient la liste des questions répondue par chaque user
            #il faut ensuite que je compte pour chaque reponse possible le nombre de réponse qu'il y a eu en totale

        context = {
            "nombre_reponse0": 0,
            "nombre_reponse1": 0,
            "nombre_reponse2": 0,
            "nombre_reponse3": 0,
            "nombre_tot":0,
        }
        for user in User.objects.all().filter(id_quizz=id_quizz):
            for i in range(0,4): #pour les 3 reponses possibles
                if int(question_answered)==i:
                    context["nombre_reponse"+str(i)]+=1 # on incrémente de 1 si on a repondu la reponse i
                    context["nombre_tot"] += 1
                    break
        print(context)
        return render(request, 'quizz/userAnswered_resultat.html',context)
    if request.method=='POST':
        return HttpResponseRedirect("/interfaceUser/" + "pseudo=" + str(pseudo) + "/id=" + id_quizz + "/num_question="+str(int(num_question)+1)) #enelver 127....

def erreurPseudo(request):
    return render(request, 'quizz/erreurPseudo.html')




#comment faire pour lancer le quizz à distance ???
#variable onGame qui est a false tout le temps et requete ajax qui modifie les données serveur pour la mettre en True, en meme temps, un script javascript est executé
#qui attend que la div contenant le context on game passe a true puis redirige
