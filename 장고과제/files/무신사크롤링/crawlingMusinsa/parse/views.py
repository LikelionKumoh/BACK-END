from urllib.request import urlopen
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import Searchform
from parse import parsing

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}



def home(request):
    if request.method == 'POST':
        form = Searchform(request.POST)
        searchword= request.POST.get('search')
        if form.is_valid():
            url= 'https://www.musinsa.com/search/musinsa/integration?type=&q='+searchword
            response=requests.get(url)
            resdata=response.url
            return render(request,'search.html',{'resdata':resdata})
    else:
        form = Searchform()
        items=parsing.crawling()

            

    return render(request, 'index.html', {'items':items,'form':form})
