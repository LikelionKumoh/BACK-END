from django.shortcuts import render, redirect, get_object_or_404
from main.forms import MemoForm
from main.models import Memo



def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('main')
    else : 
        form = MemoForm()
    return render(request, 'create.html', {'form' : form})

def detail(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'detail.html', {'memo_detail' : memo_detail})

