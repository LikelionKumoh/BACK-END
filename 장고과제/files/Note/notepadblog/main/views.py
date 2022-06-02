from pydoc import pager
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notepad
from django.utils import timezone
from .forms import NoteForm
from django.core.paginator import Paginator

def home(request):
    posts = Notepad.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5)
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request,'index.html',{'posts':posts})

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'create_memo.html', {'form':form})

def detail(request, Note_id):
    note_detail = get_object_or_404(Notepad, pk=Note_id)
    return render(request, 'detail.html', {'note_detail':note_detail})