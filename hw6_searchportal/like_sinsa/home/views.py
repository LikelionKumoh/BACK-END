import re
from django.shortcuts import render
from django.http import HttpResponse
from .crawltest import get_data
from .models import Goods

# Create your views here.

def home(request):
    return render(request, 'main.html')


def search(request, choice, text):
    Goods.objects.all().delete()
    get_data(text, choice)
    goods_list = Goods.objects.all()
    context = {'goods_list': goods_list}
    return render(request, 'show.html', context)