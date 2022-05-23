from django.shortcuts import render

def home(request):
    return render(request, 'kit/home.html')

def kit(request):
    return render(request, 'kit/kit.html')

def computer(request):
    return render(request, 'kit/computer.html')

def backEnd(request):
    return render(request, 'kit/backEnd.html')

def frontEnd(request):
    return render(request, 'kit/frontEnd.html')

def pmDesign(request):
    return render(request, 'kit/pmDesign.html')

def likelion(request):
    return render(request, 'kit/likelion.html')

def mypage(request):
    return render(request, 'kit/mypage.html')
