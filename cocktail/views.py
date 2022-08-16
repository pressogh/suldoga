from django.shortcuts import render,redirect, get_object_or_404
from .models import Cocktail, Like, Star
from django.core.paginator import Paginator


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



def LikeView(request, cocktail_id):
    like_c = get_object_or_404(Cocktail, id=cocktail_id)

    if request.user in like_c.likes.all():
        like_c.likes.remove(request.user)
        like_c.like_count -= 1
        like_c.save()

    else:
        like_c.likes.add(request.user)
        like_c.like_count += 1
        like_c.save()
        
    return redirect('cocktail/:test2', like_c.id)



def index(request):
    sort = request.GET.get('sort','')
    paginator = Paginator(cocktail_list,'10')
    page = request.GET.get('page','')
    posts = paginator.get_page(page)

    if sort == 1: #기본
        cocktail_list= Cocktail.objects.order_by('')

    elif sort == 2: #별점순
        cocktail_list = Cocktail.objects.annotate(star_count=Cocktail('stars')).order_by('-star_count')
        
    elif sort == 3: #스크랩순
        cocktail_list = Cocktail.objects.annotate(like_count=Cocktail('likes')).order_by('-like_count')

    elif sort == 4: #도수순
        cocktail_list = Cocktail.objects.order_by('alcohol')


    elif sort == 5: #최신순
        cocktail_list = Cocktail.objects.filter(name_id = user).order_by('-date') 
 

    elif sort == 6: #여성인기
        cocktail_list = Cocktail.objects.order_by('')

    else: #남성인기
        cocktail_list = Cocktail.objects.order_by('')
        return render(request, 'cocktail/cocktail.html', {"cocktail": cocktail_list})

    