from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Pin
from administrateur.models import Quizz

@csrf_protect
def index(request):

    if request.method == 'POST':
        ID= request.POST.get('id')
        quizzs=Quizz.objects.all()
        a=False
        for quizz in quizzs: #améliorable
            if str(quizz.id)==ID:
                a=True
                break
        if a==False:
            pin = Pin(id=ID)
            pin.save()
            return HttpResponseRedirect('/erreurId/') ##faire autre methode pour afficher l'erreur sans renvoyer sur une autre page
        return HttpResponseRedirect('/waitingpageUser0/'+'id='+ID) # choisi son pseudo, pour l'instant je renvoie directre sur la page, a voir comment on peut avoir
    return render(request, 'OpenQuizz/index.html')

def erreurId(request):
    return render(request, 'OpenQuizz/erreurId.html')
