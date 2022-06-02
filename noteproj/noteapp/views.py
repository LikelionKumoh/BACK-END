from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Memo
from django.utils import timezone
from .forms import MemoForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # posts = Blog.objects.all()
    posts = Memo.objects.filter().order_by('-date')
    paginator = Paginator(posts,5)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request,'index.html',{'posts':posts})


def newmemo(request):
    if request.method == 'POST':
        form  = MemoForm(request.POST) 
        if form.is_valid():
            #저장해라
            post = Memo()
            post.title = form.cleaned_data['body'][:10] 
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:#입력을 받을 수 있는 html 갖다주기
        form  = MemoForm() 
    return render(request,'newmemo.html',{'form':form})#render 함수의 3번째 인자를 이용해서 views.py내의 데이터(form)을 html 에 넘겨줄 수 있다. 딕셔너리 자료형으로.

def detail(request,memo_id):
    #blog_id번째 블로그 글을 db 로 부터 갖고 와서 detail.html로 띄워주는 함수
    memo_detail = get_object_or_404(Memo,pk=memo_id)


    return render(request,'detail.html',{'memo_detail':memo_detail})