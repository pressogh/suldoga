from django.shortcuts import render


def MainView(request):
    return render(request, 'cocktail/main.html')
