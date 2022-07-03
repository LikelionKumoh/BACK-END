from django.shortcuts import render, redirect
from crawler.models import ClothingData
from musinsa_crawling import clothing_data

def home(request):
    return render(request, 'index.html')
    
def create(request):
    crawlingMusinsa = ClothingData.objects.all()
    crawlingMusinsa.delete()   
    musinsa_data = clothing_data()
    for data in musinsa_data:
        item = ClothingData()
        item.rank = data['rank']
        item.image = data['image']
        item.brand = data['brand']
        item.product = data['product']
        item.price = data['price']
        item.save()





