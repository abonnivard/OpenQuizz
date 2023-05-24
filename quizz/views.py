from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from administrateur.models import Quizz, Question,Association
from quizz.models import User
from django.http import JsonResponse
import time

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

def waitingpageUser1(request,pseudo,id): #fairte en sorte que des qu'on quitte la page ça supprime (en ajax ?) ça supprime l'user
    if request.method == 'POST':
        return HttpResponseRedirect("/interfaceUser/"  + str(pseudo) + "/id=" + id + "/num_question=0")

    context = {
        'id':id,
        'pseudo':pseudo,
        'url': "/interfaceUser/" + str(pseudo) + "/id=" + id + "/num_question=0"
    }

    def is_ajax():
        return request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax()==True:
        data = {
            'onGame': Quizz.objects.all().get(id=id).onGame
        }
        return JsonResponse(data)

    return render(request, 'quizz/waitingpageUser1.html',context)


@csrf_protect
def interfaceUser(request, pseudo, id_quizz, num_question):  # moyen d'afficher les questions dans le désordre ?

    if request.method == 'GET':
        quizz = Association.objects.all().filter(idQuizz=id_quizz)
        questions_id = quizz[int(num_question)].idQuestion
        l = len(quizz) - 1
        if (int(num_question) == l):
            return HttpResponseRedirect('/finQuizz/' + pseudo + "/id=" + id_quizz)
        else:
            timer = Quizz.objects.all().get(id=id_quizz).timer
            question = Question.objects.get(id=questions_id)  ##strip pour enlever tous les espaces gênants
            context = {
                'onGame': Quizz.objects.all().get(id=id_quizz).onGame,
                "pseudo": pseudo,
                "image": str(question.image),
                "question": question.enonce,
                'timer': int(timer) + 4,
                'num_question': int(num_question.split()[0]),  # seul moyen de convertire en int
                'id_quizz': id_quizz.strip(),
                'reponse1': question.reponse1,
                'reponse2': question.reponse2,
                'reponse3': question.reponse3,
                'reponse4': question.reponse4,
            }
        return render(request, 'quizz/interfaceUser.html', context)

    if request.method == 'POST':

        quizz = Association.objects.all().filter(idQuizz=id_quizz)
        questions_id = quizz[int(num_question)].idQuestion
        question = Question.objects.get(id=questions_id)  # j'obtient la liste des questions
        reponseVrai = question.reponseVrai
        L = [request.POST.get('bouton1'), request.POST.get('bouton2'), request.POST.get('bouton3'),
             request.POST.get('bouton4')]  # None="" si répondu, autre sinon
        j = 0  # jobtient le numero du bouton sur lequel l'user a appuyé grâce au naming des boutons et au valuing
        time_reponse= 0
        for i in range(0,4) :
            if L[i]!=None:
                j=i
                time_reponse=L[i]
                break
        player = User.objects.all().get(id_quizz=id_quizz,pseudo=pseudo)
        player.question += str(j) + "/"
        if int(j) + 1 == int(reponseVrai):
            player.score += 1
            player.save()
            print("score modifié")
        # dans l'url /(fin-debut)
        return HttpResponseRedirect('num_question=' + num_question + '/userAnswered/' + str(j) +'/'+ str(time_reponse))



def userAnswered(request,pseudo, id_quizz, num_question,question_answered,time_reponse):


    if request.method=='GET':
        print('time_reponse = ' +time_reponse)
        time_restant = 4 #Quizz.objects.all().get(id=id_quizz).timer - int(time_reponse)
        context = {
            'question_answered': question_answered,
            'id': id_quizz,
            'num_question': num_question,
            'pseudo': pseudo,
            'onGame' : Quizz.objects.all().get(id=id_quizz).onGame,
            'time_restant' : time_restant
        }

        return render(request, 'quizz/userAnswered.html',context)
    if request.method=='POST':
        return HttpResponseRedirect('resultat/')


def userAnswered_resultat(request,pseudo, id_quizz, num_question,question_answered):

    if request.method=='GET':

        def is_ajax():
            return request.headers.get('x-requested-with') == 'XMLHttpRequest'

        if is_ajax() == True:
            data = {
                'onGame': Quizz.objects.all().get(id=id_quizz).onGame
            }
            return JsonResponse(data)
        else : #eviter que'on modifie question a chaque requete ajax

            user = User.objects.all().get(id_quizz=id_quizz, pseudo=pseudo)
            user.question+=str(question_answered)
            user.save()

        quizz = Association.objects.all().filter(idQuizz=id_quizz)
        questions_id = quizz[int(num_question)].idQuestion
        question = Question.objects.get(id=questions_id)
        bonne_reponse = Question.objects.all().get(id=questions_id).reponseVrai
        Score = User.objects.all().get(id_quizz=id_quizz, pseudo=pseudo).score
        users = User.objects.all().filter(id_quizz=id_quizz)
        i=0
        podium = 'False'
        correct = 'False'
        if question_answered!='_': #l'user à répondu
            if int(bonne_reponse) - 1 == int(question_answered):
                correct = 'True'
        if question_answered=='_':
            correct = 'blank'
        for user in users :
            if user.score > Score :
                i+=1
        if i<3 :
            podium = 'True'
        context = {
            'id': id_quizz,
            'correct': correct,
            'podium': podium,
            'pseudo':pseudo,
            'num_question':num_question,
            'onGame': Quizz.objects.all().get(id=id_quizz).onGame
        }
        return render(request, 'quizz/userAnswered_resultat.html',context)


    if request.method=='POST':

        return HttpResponseRedirect("/interfaceUser/" + str(pseudo) + "/id=" + id_quizz + "/num_question="+str(int(num_question)+1))

def finQuizz(request,id,pseudo):
    context= {
        'score' : User.objects.all().get(id_quizz=id, pseudo=pseudo).score
    }
    User.objects.all().get(id_quizz=id,pseudo=pseudo).delete()
    Quizz.objects.all().get(id=id).onGame=0
    Quizz.objects.all().get(id=id).save()

    return render(request, 'quizz/finquizz.html')


def interfaceProf0(request, id):
    quizz = Quizz.objects.all().get(id=id)
    quizz.onGame = 1
    quizz.save()
    context = {
        'id': id
    }
    def is_ajax():
        return request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax()==True:
        data = {
        }
        users= User.objects.all().filter(id_quizz=id)
        i=0
        for user in users: #retourne tous les users
            data["user_"+str(i)]=user.pseudo
            i+=1
        return JsonResponse(data)


    if request.method=='POST':
        quizz=Quizz.objects.all().get(id=id)
        quizz.onGame+=1
        quizz.save()
        return HttpResponseRedirect('/interfaceProf1/id='+id+'/num_question=0')

    return render(request, 'quizz/interfaceProf0.html',context)

def interfaceProf1(request, id, num_question):
    if request.method=='GET':
        quizz = Association.objects.all().filter(idQuizz=id)
        questions_id = quizz[int(num_question)].idQuestion
        l=len(quizz)-1
        if (int(num_question)==l):
            return HttpResponseRedirect('/finQuizzProf/id='+str(id))
        else:
            timer =Quizz.objects.all().get(id=id).timer
            question=Question.objects.get(id=questions_id) ##strip pour enlever tous les espaces gênants
            context = {
                "image" : str(question.image),
                "question": question.enonce,
                'timer': int(timer)+4,
                'num_question': int(num_question.split()[0]), #seul moyen de convertire en int
                'id_quizz': id.strip(),
                'reponse1': question.reponse1,
                'reponse2': question.reponse2,
                'reponse3': question.reponse3,
                'reponse4': question.reponse4,
            }
        return render(request, 'quizz/interfaceProf1.html',context)
    if request.method == 'POST':
        quizz = Quizz.objects.all().get(id=id)
        quizz.onGame += 1
        quizz.save()
        return HttpResponseRedirect('num_question='+num_question+'/resultat')
    return render(request, 'quizz/interfaceProf1.html')



def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')



def resultat(request, id, num_question): #possiblité de savoir si il y a encore des joeueur à attendre
    #faire de l'ajax pour actualiser car pas de processus pour synchroniser les users parfaitements + augmenter le pooling rate
    if request.method=='GET':

        def is_ajax():
            return request.headers.get('x-requested-with') == 'XMLHttpRequest'

        if is_ajax() == True:
            quizz = Association.objects.all().filter(idQuizz=id)
            questions_id = quizz[int(num_question)].idQuestion
            question = Question.objects.get(id=questions_id)
            bonne_reponse = Question.objects.all().get(id=questions_id).reponseVrai
            data = {
                "nombre_reponse0": 0,
                "nombre_reponse1": 0,
                "nombre_reponse2": 0,
                "nombre_reponse3": 0,
                "nombre_tot": 0,
                "bonne_reponse": bonne_reponse,
            }
            for user in User.objects.all().filter(id_quizz=id): #pour faire comme kahoot en montrer la proportion des reponses des autres
                questions=user.question
                L=questions.split("/") # j'obtient la liste des questions répondue par chaque user
                print(L)
                if L[int(num_question)]=='0':
                    data["nombre_reponse0"]+=1
                    data["nombre_tot"] += 1
                if L[int(num_question)]=='1':
                    data["nombre_reponse1"]+=1
                    data["nombre_tot"] += 1
                if L[int(num_question)]=='2':
                    data["nombre_reponse2"]+=1
                    data["nombre_tot"] += 1
                if L[int(num_question)]=='3':
                    data["nombre_reponse3"]+=1
                    data["nombre_tot"] += 1
                if L[int(num_question)]=="_":
                    data["nombre_tot"]+=1
            return JsonResponse(data)

        quizz = Association.objects.all().filter(idQuizz=id)
        l = len(quizz) - 1
        if (int(num_question) == l):
            return HttpResponseRedirect('/finQuizzProf/id=' + id)
        else:
            questions_id = quizz[int(num_question)].idQuestion
            question = Question.objects.get(id=questions_id)
            bonne_reponse = Question.objects.all().get(id=questions_id).reponseVrai
            context = {
                "nombre_reponse0": 0,
                "nombre_reponse1": 0,
                "nombre_reponse2": 0,
                "nombre_reponse3": 0,
                'reponse1': question.reponse1,
                'reponse2': question.reponse2,
                'reponse3': question.reponse3,
                'reponse4': question.reponse4,
                "nombre_tot": 0,
                "bonne_reponse": bonne_reponse
            }
            return render(request, 'quizz/resultat.html',context)
    if request.method=='POST':
        quizz = Quizz.objects.all().get(id=id)
        quizz.onGame += 1
        quizz.save()
        return HttpResponseRedirect("/interfaceProf1/id=" + id + "/num_question="+str(int(num_question)+1))


def finQuizzProf(request,id):
    if request.method=='GET':


        top1=top2=top3 = None

        for user in User.objects.all().filter(id_quizz=id): #prend les 3 plus gros scores


            if top1 is None or user.score >= top1.score:
                top3 = top2
                top2 = top1
                top1 = user
            elif top2 is None or user.score >= top2.score:
                top3 = top2
                top2 = user
            elif top3 is None or user.score >= top3.score:
                top3 = user
        if top1 == None : # 0 joueur
            context ={}
        if top2 == None : # 1 joueur
            context = {
                'top1': top1.pseudo,
            }
        if top3 ==None : #2 joeuurs
            context= {
                'top1': top1.pseudo,
                'top2': top2.pseudo,
            }
        else :  #3 joueurs
            context = {
                'top1': top1.pseudo,
                'top2': top2.pseudo,
                'top3': top3.pseudo,
            }
        return render(request, 'quizz/finQuizzProf.html',context)
    if request.method=='POST':

        return HttpResponseRedirect("/")

    return render(request, 'quizz/finQuizzProf.html')

def erreurPseudo(request):
    return render(request, 'quizz/erreurPseudo.html')



## Petit Point :
#l'user ne connait pas le nombre de question contrairement a interfaceProf1
#interfaceProf1 prend en arg num_question, il se contente de retourner onGame+1 tant qu'il y a des questions dès qu'il veut passer à la question suivante
#ou que le temps imparti est écoulé
#pdt ce temps interfaceUser attend que onGame_num_question passe a onGame_num_question+1, dès lors il passe à la question suivante
#si l'interfaceProf renvoie onGame_FIN c'est la fin du quizz, l'interface user redirige vers finQuizz et l'interfaceProf vers finQuizzProf

#etape interface prof
#1) afficher question
#2) afficher bonne question + proportion reponse
#3) afficher podium
#4) declancher nouvelle réponse

#etape interface user
#1) afficher les possibilité de réponse
#2) afficher si on a la bonne reponse
#3) lancer la prochaine question


#A penser :
##gerer lef ait qui si le prof quitte la game -> ça pose onGame=False ? ou ça deroule de maniere auto et a la fin ca
# onGame=False ainsi que si l'eleve quitte la game, son pseudo est suppr (surtt)
#utiliser ajax quand on veut tester si le psuedo est deja pris ou pas pour ne pas ra
#afficher le nombre de personnes qui ont répondu sur interface prof
#si toutes les users ont répondu -> on affiche directe les resultats on attend pas la fin
#possibilité de choisir si le prof à un projo ou pas -> change le display le cas echéant


