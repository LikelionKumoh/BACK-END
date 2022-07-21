from django.apps import AppConfig

class SearchappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'searchapp'
 
    def ready(self):
        from searchapp.models import SearchModel
        import os 
        from tokenize import Name
        import requests
        from bs4 import BeautifulSoup

        if not os.environ.get('App'):
            os.environ['APP']='True'
            #크롤링 기본 설정
            url="https://www.musinsa.com/ranking/best?u_cat_cd="
            response=requests.get(url)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            #크롤링 본문
            data_list=soup.select('#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a')
            n=1
            for _ in data_list:
                name=soup.select_one('#goodsRankList > li:nth-child('+str(n)+') > div.li_inner > div.article_info > p.list_info > a')['title']
                id=soup.select_one('#goodsRankList > li:nth-child('+str(n)+')')['data-goods-no']
                rank=soup.select_one('#goodsRankList > li:nth-child('+str(n)+') > p').get_text().split()[0]
                image=soup.select_one('#goodsRankList > li:nth-child('+str(n)+') > div.li_inner > div.list_img > a > img')['data-original'] #태그 안에 내용이 있음.
                brand=soup.select_one('#goodsRankList > li:nth-child('+str(n)+') > div.li_inner > div.article_info > p.item_title > a').get_text()
                price=soup.select_one('#goodsRankList > li:nth-child('+str(n)+') > div.li_inner > div.article_info > p.price').get_text().split()
                if(len(price) == 1):
                    price=price[0]
                else:
                    price=price[1]   
                SearchModel(InfoId=id, Name=name, Rank=rank, Image=image, Brand=brand,Price=price).save()
                n=n+1
                #likecount=soup.select_one('#like_2439314')#???태그 안에 안나타남
