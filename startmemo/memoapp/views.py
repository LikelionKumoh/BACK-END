from django.shortcuts import render, redirect, get_object_or_404
from memoapp.forms import MemogModelForm
from memoapp.models import Memo
from django.core.paginator import Paginator

def home(request):
    # posts = Memo.objects.all()
    posts = Memo.objects.filter().order_by('-date')
    paginator = Paginator(posts,5)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'home.html', {'posts':posts})

# 메모 저장
def modelformcreate(request):
    if request.method == 'POST' or request.method=='FILES':
        #입력 내용을 DB에 저장
        form = MemogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html 갖다주기
        form = MemogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk=memo_id)
    # comment_form = CommentForm()
    return render(request, 'detail.html', {'memo_detail':memo_detail})

#{'comment_form':comment_form}

# def new_comment(request, memo_id):
#     filled_form = CommentForm(request.POST)
#     if filled_form.is_valid():
#         finished_form = filled_form.save(commit=False)
#         finished_form.post = get_object_or_404(Memo, pk=memo_id)
#         finished_form.save()
#     return redirect('detail.html', memo_id)
    