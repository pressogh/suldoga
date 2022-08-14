from django.shortcuts import render
from board.forms import PostUploadForm


def ListView(request):
    if request.method == 'GET':
        return render(request, 'community/main.html')


def CreateView(request):
    if request.method == 'GET':
        form = PostUploadForm()
        return render(request, 'community/create.html', {'forms': form})


def DetailView(request, post_id):
    if request.method == 'GET':
        return render(request, 'community/detail.html')
