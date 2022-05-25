from unicodedata import name
from django.shortcuts import render
import requests
import json
from .form import SearchForm

my_id = 'f1c1da68ad162d15e8a08d6deec611e0'

def home(request):
    if request.method == 'POST':
        #입력된 내용을 바탕으로
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {"obj":obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key=' + my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request,'index.html',{'obj':obj,'form':form})

def detail(request,movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+ movie_id + '?api_key=' + my_id
    response = requests.get(url)
    resdata = response.text
    return render(request,'detail.html',{"resdata":resdata})