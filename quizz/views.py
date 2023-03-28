from django.shortcuts import render

def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')

def interfaceUser(request):
    return render(request, 'quizz/interfaceUser.html')

def waitingpageProf(request):
    return render(request, 'quizz/watingpageProf.html')

def waitingpageUser(request):
    return render(request, 'quizz/waitingpageUser.html')