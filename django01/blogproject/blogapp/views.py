
from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    return render(request, 'index.html')

#블로그 글 작성 html
def new(request):
    return render(request, 'new.html')


#블로그 글 생성 
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.reg_date = timezone.now()
        post.save()

    return redirect('home')



# django form을 이용해서 입력값을 받는 함수
# get과 (=입력값을 받을 수 있는 html을 갖다 줘야함)
# post 요청 (=입력한 내용을 디비에 저장. form에서 입력한 내용을 처리)
# 모두 처리 가능한 함수
def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data ['body']
            post.save()
            return redirect('home')


       # 입력 내용을 DB에 저장
    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogForm()
    return render(request, 'form_create.html', {'form' : form})

def modelcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect  ('home')

       # 입력 내용을 DB에 저장
    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form' : form}) 