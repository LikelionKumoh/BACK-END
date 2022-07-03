from urllib.request import urlopen
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import SearchForm

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}



def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword= request.POST.get('search')
        if form.is_valid():
            url= 'https://www.musinsa.com/search/musinsa/integration?type=&q='+searchword
            response=requests.get(url)
            resdata=response.url
            return render(request,'search.html',{'resdata':resdata})
    else:
        form = SearchForm()
        url = "https://www.musinsa.com/ranking/best?u_cat_cd="

        response=requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        items=[]
        rank_list=soup.select('li.li_box')
        for item in rank_list:
            # 이미지
            img=item.find('a',{'class':'img-block'}).find('img')
            # print(img['data-original'])

            # 랭크 크롤링
            rank=item.find('p',{'class':'n-label label-default txt_num_rank'})
            rank.find('span').decompose()
            # print(rank.text)

            # 브랜드 크롤링
            brand=item.find('p',{'class':'item_title'}).find('a')

            # 상품명
            name = item.find('p',{'class':'list_info'}).find('a')
            # 가격
            price=item.find('p',{'class':'price'})
            # 좋아요
            like=item.find('span',{'class':'count'})

            item_obj = {
                    'img': img['data-original'],
                    'rank': rank.text,
                    'brand': brand.text,
                    'name' : name.text,
                    'price' : price.text,
                    'like' : like,
                }
            items.append(item_obj)

    return render(request, 'index.html', {'items':items,'form':form})
