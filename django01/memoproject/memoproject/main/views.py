from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from django.utils import timezone
from .forms import MemoForm

def main(request):
    memos = Memo.objects.filter().order_by('-reg_date')
    return render(request, 'main.html', {'memos': memos})

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


