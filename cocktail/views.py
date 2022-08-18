from django.shortcuts import render,redirect, get_object_or_404
from .models import Cocktail
from django.core.paginator import Paginator
from accounts.models import User


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ListView(request):
    cocktail = Cocktail.objects.filter(type="C")    # 테이블의 객체 불러와서 저장
    sort = request.GET.get('sort','')    

    if sort == 1: #기본
        cocktail_list= Cocktail.objects.order_by('')
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 2: #스크랩순 (하트)
        cocktail_list = Cocktail.objects.order_by(like_count=Cocktail('likes')).order_by('-like_count')
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 3: #도수 낮은 순
        cocktail_list = Cocktail.objects.order_by('alcohol')
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 4: #도수 높은 순
        cocktail_list = Cocktail.objects.order_by('-alcohol')
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})
    
    """
    paginator=Paginator(cocktail_list,16)
    page = request.GET.get('page','')
    cocktails = paginator.get_page(page)
    """

    return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail})

    #return render(request, 'cocktail/cocktail.html', {'cocktails':cocktails,'sort':sort })


def KListView(request):
    kocktail = Cocktail.objects.filter(type="K")
    sort = request.GET.get('sort','')    

    if sort == 1: #기본
        kocktail_list= Cocktail.objects.order_by('')
        return render(request, 'cocktail/kocktail.html', {"cocktail": kocktail_list})

    elif sort == 2: #스크랩순 (하트)
        kocktail_list = Cocktail.objects.annotate(like_count=Cocktail('likes')).order_by('-like_count')
        return render(request, 'cocktail/kocktail.html', {"cocktail": kocktail_list})

    elif sort == 3: #도수 낮은 순
        kocktail_list = Cocktail.objects.order_by('alcohol')
        return render(request, 'cocktail/kocktail.html', {"cocktail": kocktail_list})

    elif sort == 4: #도수 높은 순
        kocktail_list = Cocktail.objects.order_by('-alcohol')
        return render(request, 'cocktail/kocktail.html', {"cocktail": kocktail_list})
    
    return render(request, 'cocktail/kocktail.html', {"kocktail": kocktail})


def Combination2View(request):
    return render(request, 'cocktail/combination2.html') 


def TestView(request):
    return render(request, 'cocktail/test.html')



    