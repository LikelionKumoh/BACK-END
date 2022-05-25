from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')