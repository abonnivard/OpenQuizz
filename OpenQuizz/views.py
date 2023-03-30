from django.http import HttpResponseRedirect
from django.shortcuts import render
from administrateur.models import Quizz

def index(request):

    if request.method == 'POST':
        id= request.POST.get('id')
        quizzs=Quizz.objects.all()
        bool=False
        for quizz in quizzs: #améliorable
            if quizz.id==id:
                bool=True
                break
        if bool==False:
            return HttpResponseRedirect('/erreurId/') ##faire autre methode pour afficher l'erreur sans renvoyer sur une autre page
        return HttpResponseRedirect('/interfaceLogin/')
    return render(request, 'OpenQuizz/index.html')

def erreurId(request):
    return render(request, 'OpenQuizz/erreurId.html')
#Apres avoir rentrer son