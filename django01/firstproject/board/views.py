from django.shortcuts import render

def board(request):
    return render(request, 'board/board.html')

def boardfirst(request):
    return render(request, 'board/boardfirst.html')