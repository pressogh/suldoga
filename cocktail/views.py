from unicodedata import name
from django.shortcuts import render

import cocktail

from .models import CocktailCocktail #CocktailCocktail모델 불러오기


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ModalView(request):
    return render(request, 'cocktail/modal.html')


def ListView(request):
    cocktail = CocktailCocktail.objects.filter(type="C") #테이블의 객체 불러와서 저장
    return render(request, 'cocktail/cocktail.html', {"cocktail":cocktail})


def KListView(request):
    kocktail = CocktailCocktail.objects.filter(type="K") 
    return render(request, 'cocktail/kocktail.html', {"kocktail":kocktail})

