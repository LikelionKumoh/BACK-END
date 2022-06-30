from django.shortcuts import render
import requests
from .forms import SearchForm
from bs4 import BeautifulSoup
from .models import Product


def home(request):
    if request.method =='POST':  
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://www.musinsa.com/search/musinsa/integration?type=&q='+searchword
            esponse = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select("#goodsRankList > li")
        info = []
        for element in elements:
            list = {}
            rank = element.select_one("#goodsRankList > li > p").text
            img = element.select_one("#goodsRankList > li > div.li_inner > div.list_img > a > img")['data-original']
            brand = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.item_title > a").text
            name = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a")["title"]
            price = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.price").text
            list['rank'] = rank
            list['img'] = img
            list['brand'] = brand
            list['name'] = name         
            list['price'] = price
            info.append(list)
        
        for dict in info:
            Product(name = dict["name"], rank = dict["rank"], img =  dict["img"], brand = dict["brand"], price = dict["price"]).save()
                          
        return render(request, 'search.html', {'Product':Product})
    else:    
        form = SearchForm()    
        url="https://www.musinsa.com/ranking/best?u_cat_cd="    
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select("#goodsRankList > li")
        info = []
        for element in elements:
            list = {}
            rank = element.select_one("#goodsRankList > li > p").text
            img = element.select_one("#goodsRankList > li > div.li_inner > div.list_img > a > img")['data-original']
            brand = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.item_title > a").text
            name = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a")["title"]
            price = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.price").text
            list['rank'] = rank
            list['img'] = img
            list['brand'] = brand
            list['name'] = name         
            list['price'] = price
            info.append(list)
            
        
        
        for dict in info:
            Product(name = dict["name"], rank = dict["rank"], img =  dict["img"], brand = dict["brand"], price = dict["price"]).save()
                
    return render(request, 'index.html',{'Product':Product,'form':form})
