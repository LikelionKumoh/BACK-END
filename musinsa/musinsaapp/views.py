from django.shortcuts import render, get_object_or_404
from .forms import SearchForm, ProductForm
from .models import Product



def home(request):
    if request.method =='POST':  
        form = SearchForm(request.POST)
        search = request.POST.get('search')
        products = Product.objects.filter(name__icontains=search) |Product.objects.filter(brand__icontains=search)
        return render(request, 'search.html', {'products':products,'search':search})
    else:    
        form = SearchForm()
        products = Product.objects.all()      
        return render(request, 'index.html',{'products':products, 'form':form})
