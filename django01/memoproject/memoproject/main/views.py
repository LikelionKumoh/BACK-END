from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    memo_all = Memo.objects.filter().order_by('-reg_date')
    paginator = Paginator(memo_all, 5)
    page = request.GET.get('page',  1)

    try :
        posts = paginator.page(int(page))
        context = {
            'page' : posts,
        }
    except EmptyPage:
        return redirect('/')

    return render(request, 'main.html', context)

