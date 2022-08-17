from django.shortcuts import render, get_object_or_404, redirect
from .models import Cocktail
from accounts.models import User


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ListView(request):
    cocktail = Cocktail.objects.filter(type="C")    # 테이블의 객체 불러와서 저장
    return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail})


def KListView(request):
    kocktail = Cocktail.objects.filter(type="K")
    return render(request, 'cocktail/kocktail.html', {"kocktail":kocktail})


def TestView(request):
    return render(request, 'cocktail/test.html')


def LikeView(request, cocktails_id):
    like_b = get_object_or_404(Cocktail, id=cocktails_id)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('cocktail/main.html' + str(cocktails_id))

def myprofile(request,user_id):  
    user = User.objects.get(id = user_id)
    cocktail_likes = user.likes.all()
    context={
        "cocktail_likes":cocktail_likes,
    }
    return render(request, 'myprofile.html',context)