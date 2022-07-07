from django.shortcuts import render, redirect
from .models import ClothingData
from .musinsa_crawling import clothing_data
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def home(request):
    item_detail = ClothingData.objects.all()
    if request.method == 'POST':
        q = request.POST.get('q','') # 검색어 가져오기
        if q: # 만약 검색어가 존재하면
            item_detail = item_detail.filter(brand__icontains=q)|item_detail.filter(product__icontains=q) # 해당 검색어를 포함한 queryset 가져오기
            return render(request, '../templates/index.html', {'item_detail':item_detail})
    else:
        return render(request, '../templates/index.html', {'item_detail':item_detail}) 

def create():
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


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordcheck']:
            user = User.objects.create(
                username=request.POST['username'],
                password=request.POST['password'],
                name=request.POST['name'],
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, '../templates/signup.html')
    return render(request, '../templates/signup.html')
     
def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, '../templates/index.html')

    # GET 요청이 들어오면 login form 을 담고있는 login.html을 띄워주는 역할을 함
    else:
        return render(request, '../templates/index.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


