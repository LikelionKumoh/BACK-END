from django.shortcuts import render, redirect
from django.http import HttpResponse

from .crawltest import get_data
from .models import Goods


# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def search(request, choice, text):
    Goods.objects.all().delete()
    get_data(text, choice)
    goods_list = Goods.objects.all()
    context = {'goods_list': goods_list}
    return render(request, 'home/show.html', context)