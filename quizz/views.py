from django.shortcuts import render

def interfaceProf(request):
    return render(request, 'quizz/interfaceProf.html')

def interfaceUser(request):
    return render(request, 'quizz/interfaceUser.html')
