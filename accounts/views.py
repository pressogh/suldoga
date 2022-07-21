from django.shortcuts import render


def LoginView(request):
    return render(request, 'accounts/login.html')


def RegisterView(request):
    return render(request, 'accounts/register.html')