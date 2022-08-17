from django.shortcuts import render
from .models import Cocktail


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ListView(request):
    cocktail = Cocktail.objects.filter(type="C")    # 테이블의 객체 불러와서 저장
    return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail})


def KListView(request):
    kocktail = Cocktail.objects.filter(type="K")
    return render(request, 'cocktail/kocktail.html', {"kocktail": kocktail})


def TestView(request):
    return render(request, 'cocktail/test.html')
