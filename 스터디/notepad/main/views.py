from django.shortcuts import render
from memo.models import Memo
from django.core.paginator import Paginator

def main(request):
    memo = Memo.objects.filter().order_by('-date')
    paginator = Paginator(memo,5)
    pagenum = request.GET.get('page')
    memo = paginator.get_page(pagenum)
    return render(request,'index.html', {'memo':memo})