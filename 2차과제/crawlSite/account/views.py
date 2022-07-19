from django.shortcuts import render
from requests import request
from .models import Member

def signup(request):
    if(request.method == 'POST'):
        member = Member()
        if(not Member.objects.filter(username=request.POST['username']).exists()):
            member.username = request.POST['username']
            member.password = request.POST['password']
            member.save()
            return render(request,'account/signup_success.html')
        else:
            return render(request,'account/signup_error.html')
    elif(request.method == 'GET'):
        return render(request, 'account/signup.html')

def login(request):
    if(request.method == 'POST'):
        member = Member()
        if(Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists()):
            return render(request,'account/login_success.html')
        else:
            return render(request,'account/login_error.html')
    elif(request.method == 'GET'):
        return render(request,'account/login.html')
