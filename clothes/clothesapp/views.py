from django.shortcuts import render
from .forms import ProductModelForm
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        products = Product.objects.filter(name__contains=searched) | Product.objects.filter(brand__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'products':products})
    else:
        return render(request, 'search.html', {})