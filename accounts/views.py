from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from OpenQuizz.views import index
from .forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            username = request.POST['username']
            user = authenticate(request, email=email, password=password, username=username)
            if user is not None:
                login(request, user)
            if request.user.is_authenticated:
                return redirect(index)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
