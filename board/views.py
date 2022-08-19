from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostUpdateForm, PostUploadForm
from django.utils import timezone


def ListView(request):
    board_list = Post.objects.all().order_by('-created_at')
    context = {'board_list': board_list}
    return render(request, 'board/board.html', context)


@login_required
def PostCreateView(request):
    if request.method == 'POST':
        form = PostUploadForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('board:board')
    else:
        form = PostUploadForm()
    context = {'form': form}
    return render(request, 'board/regist.html', context)


@login_required
def DetailView(request, post_id):
    board_list = get_object_or_404(Post, id=post_id)
    context = {'board_list': board_list}
    return render(request, 'board/detail.html', context)


def UpdateView(request, post_id):
    board_list = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = PostUpdateForm(request.POST)
        if form.is_valid():
            board_list.title = request.POST['title']
            board_list.content = request.POST['content']
            board_list.created_at = timezone.now()
            board_list.save()
            return redirect('board/detail/' + str(board_list.id))
    else:
        form = PostUpdateForm(instance=board_list)
        return render(request, 'board/update.html', {'form': form})


def DeleteView(request, post_id):
    board_list = Post.objects.get(id=post_id)
    board_list.delete()
    return redirect('board:board')
