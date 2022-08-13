from django.shortcuts import get_object_or_404, render, redirect
from .models import Board
from .forms import RegistForm

# Create your views here.

def BoardView(request):
    board_list = Board.objects.all().order_by('-date')
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
    context = {'form': form}
    return render(request, 'board/regist.html', context)    

def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list': board_list}
    return render(request, 'board/detail.html', context)
