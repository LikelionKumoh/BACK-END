from django.shortcuts import render

def home(request):
    return render(request, 'cafeapp/index.html')


def detail(request):
    return render(request, 'cafeapp/portfolio-details.html')