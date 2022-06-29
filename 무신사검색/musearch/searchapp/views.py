from tokenize import Name
from django.shortcuts import render
from .forms import SearchForm
from .models import SearchModel
from django.db.models import Q

def home(request):
    form=SearchForm()
    obj=SearchModel.objects.all()
    if request.method=='POST':
        form=SearchForm(request.POST)
        searchword=request.POST.get('search')
        if searchword:
            obj=obj.filter(Q(Name__contains=searchword) | Q(Brand__contains=searchword))
        return render(request, 'search.html', {'obj':obj})            
    else:                
        return render(request,'index.html',{'obj':obj,'form':form})
