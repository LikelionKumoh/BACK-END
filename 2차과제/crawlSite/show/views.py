from django.shortcuts import render
from .models import Table
from .crawl import crawlSite

def detail(request):
    initCrawlData()
    table_detail = Table.objects.all()
    if request.method == 'GET':
        return render(request, 'table.html', {'table_detail':table_detail})
    else:
        q = request.POST.get('q',"")
        if q:
            table_detail = table_detail.filter(brand__icontains=q)
            return render(request, 'table.html', {'table_detail':table_detail})

def initCrawlData():
    allData = Table.objects.all()
    allData.delete()
    crawl_data = crawlSite()
    for data in crawl_data:
        table = Table()
        table.rank = data['rank']
        table.img = data['img']
        table.brand = data['brand']
        table.item = data['item']
        table.price = data['price']
        table.save()
