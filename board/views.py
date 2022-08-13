from django.shortcuts import render


def ListView(request):
    if request.method == 'GET':
        return render(request, 'community/main.html')


def CreateView(request):
    if request.method == 'GET':
        return render(request, 'community/create.html')


def DetailView(request, post_id):
    if request.method == 'GET':
        return render(request, 'community/detail.html')
