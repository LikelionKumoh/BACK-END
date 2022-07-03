from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')