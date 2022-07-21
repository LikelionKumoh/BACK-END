from django.shortcuts import get_object_or_404, redirect, render
from noteapp.forms import PostForm
from .models import Post
from django.core.paginator import Paginator
from django.utils import timezone

def index(request):
    posts=Post.objects.filter().order_by('-date')
    paginator=Paginator(posts,5)
    pagnum = request.GET.get("page")
    posts=paginator.get_page(pagnum)
    return render(request,'index.html',{'posts':posts})

def postcreate(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=Post()
            post.title=form.cleaned_data['body'][:10]
            post.body=form.cleaned_data['body']
            post.date=timezone.now()
            post.save()
            return redirect('index')
    else:
        form=PostForm()
    return render(request, 'postcreate.html',{'form':form})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post_detail':post_detail})