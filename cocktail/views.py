from django.shortcuts import render, get_object_or_404, redirect
from .models import Cocktail
from accounts.models import User


def MainView(request):
    cocktail = Cocktail.objects.all()
    return render(request, 'cocktail/main.html', {"cocktail": cocktail})


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ListView(request):
    cocktail = Cocktail.objects.filter(type="C")    # 테이블의 객체 불러와서 저장
    return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail})


def KListView(request):
    kocktail = Cocktail.objects.filter(type="K")
    return render(request, 'cocktail/kocktail.html', {"kocktail":kocktail})

def Combination2View(request):
    return render(request, 'cocktail/combination2.html') 


def TestView(request):
    return render(request, 'cocktail/test.html')


def LikeView(request, cocktails_id):
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
        return redirect('cocktail:main')
    return redirect('accounts:login') 

def myprofile(request,user_id):  
    user = User.objects.get(id = user_id)
    cocktails = user.like.all()
    context={
        "cocktails":cocktails
    }
    return render(request, 'cocktail/myprofile.html',context)