from django.shortcuts import render
from memos.models import Memo
from django.core.paginator import Paginator

def home(request):
    posts = Memo.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'index.html', {'posts':posts})