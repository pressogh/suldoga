from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('cocktail:main'))
        else:
            return render(request,'accounts/login.html')

    #if request.method == 'GET':
    else:
        return render(request, 'accounts/login.html')


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('cocktail:main'))

    
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cocktail:main'))
            print(user)

        return render(request, 'accounts/register.html', {'form': form})

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
