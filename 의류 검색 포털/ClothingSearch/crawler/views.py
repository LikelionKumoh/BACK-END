from django.shortcuts import render, redirect
from .models import ClothingData

def home(request):
    return render(request, 'index.html')
    
def create(request):
    crawlingMusinsa = ClothingData.objects.all()
    crawlingMusinsa.delete()
    for data in crawling:
        item = ClothingData()
        item.rank = data['rank']
        item.image = data['image']
        item.brand = data['brand']
        item.product = data['product']
        item.price = data['price']
        item.save()





