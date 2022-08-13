from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import RegistForm

def BoardView(request):
    board_list = Post.objects.all().order_by('-created_at')
    context = {'board_list': board_list}
    return render(request, 'board/board.html', context)


def regist(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('board:board')
    else:
        form = RegistForm()
    context = {'form': form,}
    return render(request, 'board/regist.html', context)

def detail(request, pk):
    board_list = get_object_or_404(Post, id=pk)
    context = {'board_list': board_list}
    return render(request, 'board/detail.html', context)
