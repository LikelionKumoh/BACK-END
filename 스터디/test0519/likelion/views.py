from django.shortcuts import render

def home(request):
    return render(request,'likelion/index.html')
