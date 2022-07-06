from django.shortcuts import render, redirect
from .forms import UserForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    form=UserForm
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'form' : form, 'status': 'fail'})
    else:
        return render(request, 'login.html',{'form' : form})
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
        
def signup(request):
    form=CreateUserForm
    #아이디 중복체크
    if request.method=='POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'signup.html', {'form' : form, 'status': 'duplicate'})
        #처음 입력한 비밀번호와 두번째로 입력한 비밀번호가 일치할 때
        if request.POST['password'] == request.POST['check_Password']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form' : form, 'status': 'diff'})
    else:    
        return render(request, 'signup.html',{'form': form})