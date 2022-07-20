from django.shortcuts import render
from .models import ClothingData
from account.models import User
from .musinsa_crawling import clothing_data

def home(request):
    create()
    item_detail = ClothingData.objects.all()
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            q = request.POST.get('q','') # 검색어 가져오기
            if q: # 만약 검색어가 존재하면(브랜드, 상품)
                item_detail = item_detail.filter(brand__icontains=q)|item_detail.filter(product__icontains=q) # 해당 검색어를 포함한 queryset 가져오기
                return render(request, 'crawler/index.html', {'item_detail':item_detail, 'user':user})
            else:
                return render(request, 'crawler/index.html', {'item_detail':item_detail, 'user':user}) 
        return render(request, 'crawler/index.html', {'item_detail':item_detail, 'user':user})    
    return render(request, 'account/login.html', {'item_detail':item_detail}) 

   
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




