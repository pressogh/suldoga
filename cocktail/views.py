from django.shortcuts import render, get_object_or_404, redirect
from .models import Cocktail
from accounts.models import User


def MainView(request):
    cocktail = Cocktail.objects.all()
    return render(request, 'cocktail/main.html', {"cocktail": cocktail})

def InfoView(request):
    return render(request, 'cocktail/info.html')

def base_wisky(request):
    return render(request, 'cocktail/wisky.html')

def base_jin(request):
    return render(request, 'cocktail/jin.html')

def base_tequila(request):
    return render(request, 'cocktail/tequila.html')

def base_vodka(request):
    return render(request, 'cocktail/vodka.html')

def base_liqueur(request):
    return render(request, 'cocktail/liqueur.html')

def base_rum(request):
    return render(request, 'cocktail/rum.html')

def base_brandy(request):
    return render(request, 'cocktail/brandy.html')

def ListView(request):
    if request.method == "GET":
        cocktail = Cocktail.objects.filter(type="C")    # 테이블의 객체 불러와서 저장
        print(request.GET)
        if request.GET:
            sort = int(request.GET["sort-type"])
        else:
            sort = 1

        cocktail_list = cocktail
        print(sort)
        if sort == 1: #기본
            cocktail_list = cocktail

        elif sort == 2: #스크랩순 (하트)
            cocktail_list = cocktail.order_by('-like_count')

        elif sort == 3: #도수 낮은 순
            cocktail_list = cocktail.order_by('alcohol')

        elif sort == 4: #도수 높은 순
            cocktail_list = cocktail.order_by('-alcohol')

        print(cocktail_list)
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list, "sort": str(sort)})


def KListView(request):
    if request.method == "GET":
        kocktail = Cocktail.objects.filter(type="K")    # 테이블의 객체 불러와서 저장
        print(request.GET)
        if request.GET:
            sort = int(request.GET["sort-type"])
        else:
            sort = 1

        kocktail_list = kocktail
        print(sort)   
        if sort == 1: #기본
            kocktail_list = kocktail

        elif sort == 2: #스크랩순 (하트)
            kocktail_list = kocktail.order_by('-like_count')

        elif sort == 3: #도수 낮은 순
            kocktail_list = kocktail.order_by('alcohol')

        elif sort == 4: #도수 높은 순
            kocktail_list = kocktail.order_by('-alcohol')

        print(kocktail_list)
        return render(request, 'cocktail/kocktail.html', {"kocktail": kocktail_list, "sort": str(sort)})

def Combination1View(request):
    return render(request, 'cocktail/combination1.html')

def Combination2View(request):
    return render(request, 'cocktail/combination2.html') 

def Combination3View(request):
    return render(request, 'cocktail/combination3.html')

def CombinationFinView(request):
    return render(request, 'cocktail/combinationFin.html') 

def TestView(request):
    return render(request, 'cocktail/test.html')


def LikeView(request, cocktails_id, next_page):
    if request.user.is_authenticated:
        cocktails = get_object_or_404(Cocktail, id=cocktails_id)

        if cocktails.like.filter(id=request.user.id).exists():
            cocktails.like.remove(request.user)
            cocktails.like_count -= 1
            cocktails.save()
        else:
            cocktails.like.add(request.user)
            cocktails.like_count += 1
            cocktails.save()
        return redirect(f'cocktail:{next_page}')

    else:
        return redirect('accounts:login')


def myprofile(request, user_id):
    user = User.objects.get(id=user_id)
    cocktails = user.like.all()
    context={
        "cocktails": cocktails
    }
    return render(request, 'cocktail/myprofile.html',context)