from django.shortcuts import render, redirect
from .models import ClothingData

def home(request):
    return render(request, 'index.html')
    
def create(request):
    if(request.method == 'POST' or request.method == 'FILES') :
        post = ClothingData()
        post.rank = request.POST['rank']
        post.image = request.FILES['image']
        post.brand = request.POST['brand']
        post.product = request.POST['product']
        post.price = request.POST['price']
        post.save()





