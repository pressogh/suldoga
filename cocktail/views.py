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
        #return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 2: #스크랩순 (하트)
        cocktail_list = Cocktail.objects.order_by(like_count=Cocktail('likes')).order_by('-like_count')
        #return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 3: #도수 낮은 순
        cocktail_list = Cocktail.objects.order_by('alcohol')
        #return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    elif sort == 4: #도수 높은 순
        cocktail_list = Cocktail.objects.order_by('-alcohol')
        #return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    paginator=Paginator(cocktail_list,16)
    page = request.GET.get('page','')
    cocktails = paginator.get_page(page)

    #return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail})

    return render(request, 'cocktail/cocktail.html', {'cocktails':cocktails,'sort':sort })


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


"""def LikeView(request, cocktail_id):
    like_c = get_object_or_404(Cocktail, id=cocktail_id)

    if request.user in like_c.likes.all():
        like_c.likes.remove(request.user)
        like_c.like_count -= 1
        like_c.save()

    else:
        like_c.likes.add(request.user)
        like_c.like_count += 1
        like_c.save()
        
    return redirect('cocktail/test2', like_c.id)

"""
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

    