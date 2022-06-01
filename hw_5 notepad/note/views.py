from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from .forms import MemoModelForm
from django.core.paginator import Paginator


def home(request):
    page = request.GET.get('page', '1')
    memo_list = Memo.objects.order_by('-date')
    paginator = Paginator(memo_list, 10)
    page_obj = paginator.get_page(page)
    content = {'memo_list': page_obj}
    return render(request, 'note/home.html', content)


def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    content = {'memo': memo}
    return render(request, 'note/detail.html', content)


def create(request):
    if request.method == 'POST':
        form = MemoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note:home')
    else:
        form = MemoModelForm()
    return render(request, 'note/form_create.html', {'form':form})

