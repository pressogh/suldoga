from django.shortcuts import render


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ListView(request):
    return render(request, 'cocktail/cocktail.html')


def KListView(request):
    return render(request, 'cocktail/kocktail.html')


def TestView(request):
    return render(request, 'cocktail/test.html')
