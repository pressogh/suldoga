from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UserSurvey


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.login(request)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cocktail:main'))
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': '아이디 또는 패스워드가 틀렸습니다.'})

        return render(request, 'accounts/login.html', {'form': form})

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


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
                return HttpResponseRedirect(reverse('accounts:survey'))

        return render(request, 'accounts/register.html', {'form': form})

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def SurveyView(request):
    if request.method == 'GET':
        return render(request, 'accounts/survey.html')

    elif request.method == 'POST':
        alcohol_type = int(request.POST['alcohol-type'])
        sweet_type = int(request.POST['sweet-type'])
        degree_type = int(request.POST['degree-type'])

        user = request.user
        model = UserSurvey(user=user, type=alcohol_type, sweet=sweet_type, degree=degree_type)
        model.save()

        return HttpResponseRedirect(reverse('cocktail:main'))
