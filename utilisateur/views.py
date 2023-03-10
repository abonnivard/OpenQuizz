from django.shortcuts import render

def waitingpage(request):
    return render(request, "utilisateur/waitingpage.html")