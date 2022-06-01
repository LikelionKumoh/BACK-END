from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from django.utils import timezone
from .forms import MemoForm

def write(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = MemoForm(request.POST)
        if form.is_valid():
            post = Memo()
            post.title = form.cleaned_data['body'][:10]
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
        return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = MemoForm()
    return render(request, 'write.html', {'form':form})

def detail(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk=memo_id)

    return render(request, 'detail.html', {'memo_detail':memo_detail})