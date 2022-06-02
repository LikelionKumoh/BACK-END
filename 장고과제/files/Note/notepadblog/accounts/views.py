from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login2.html')
    else:
        return render(request, 'login2.html')

def logout(request):
    auth.logout(request)
    return redirect('home')