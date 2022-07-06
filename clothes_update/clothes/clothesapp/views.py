from django.shortcuts import render, redirect 
from .forms import ProductModelForm
from .models import Product,MyUser
from django.contrib import auth 
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def home(request):
    products = Product.objects.all()
    user_id = request.session.get('user')
    # user_id유무를 통해 login판단
    if user_id:
        user = MyUser.objects.get(pk=user_id)
        return render(request,'index.html',{'products':products,'user':user})
        # return HttpResponse(f'{user} login success')
    return render(request,'index.html',{'products':products})

    

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        products = Product.objects.filter(Q(name__contains=searched)| Q(brand__contains=searched) )  
        return render(request, 'search.html', {'searched': searched, 'products':products})
    else:
        return render(request, 'search.html', {})

def signup(request):
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2']: 
            user = MyUser.objects.create( 
                username=request.POST['username'], 
                password=request.POST['password1'], 
                email=request.POST['email'],
            )
            request.session['user'] = user.id
            return redirect('/') 
        return render(request, 'signup.html') 
    else: 
        form = UserCreationForm 
        return render(request, 'signup.html', {'form':form})

def login(request):
    #POST 요청: 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd= request.POST['password']
        if MyUser.objects.filter(username=userid).exists():
        # user = auth.authenticate(request,username=userid,password=pwd) #해당 회원이 있으면 회원(user) 객체를, 없으면 none을 반환
            getUser = MyUser.objects.get(username=userid)
            if pwd == getUser.password:
                request.session['user'] = getUser.id
                return redirect('/')
            else:
                # return render(request,'login.html') 
                return HttpResponse('비번 못찾음')   
        else:
            # return render(request,'login.html')
            return HttpResponse('아이디 못찾음')
    #GET요청: login.html 띄우기
    else:
        return render(request,'index.html')

def logout(request):
    # auth.logout(request)
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('home')
