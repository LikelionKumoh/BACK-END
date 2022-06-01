from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemoForm
from .models import Memo

def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = MemoForm(request.POST)
        if form.is_valid():
            #저장 하는 코드
            post = Memo()
            post.title = form.cleaned_data['body'][:5]
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('main')
    else:
        # 입력 내용을 받을 수 있는 html을 갖다주기
        form = MemoForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'detail.html', {'memo_detail':memo_detail})
