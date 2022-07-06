from django.shortcuts import render, redirect
from requests import RequestException
from searchapp.models import SearchModel
from .forms import UserForm, CreateUserForm
from .models import UserModel

def login(request):
    obj=SearchModel.objects.all()
    form=UserForm
    data=request.POST
    if request.method=="POST":
        #아이디가 존재하고
        if UserModel.objects.filter(username=data['username']).exists():
            getUser=UserModel.objects.get(username=data['username'])
            #비밀번호가 일치한다면
            if getUser.password==data['password']:
                return render(request, 'searchapp/index.html',{'obj':obj,'status':'login'})
            else:
                return render(request,'accounts/login.html',{'form':form,'status':'fail1'})
        else:
            return render(request,'accounts/login.html',{'form':form,'status':'fail2'})
    else:
        return render(request, 'accounts/login.html', {'form':form})
    
def logout(request):
    return redirect('/')
    
        
def signup(request):
    form=CreateUserForm
    obj=SearchModel.objects.all()
    if request.method =="POST":
        data=request.POST
        #아이디 중복체크
        if UserModel.objects.filter(username=data['username']).exists():
            return render(request, 'accounts/signup.html', {'form' : form, 'status': 'duplicate'})
        #만약 비밀번호와 두번째 비밀번호가 갔다면
        if request.POST['password'] != request.POST['checkpassword']:
            return render(request, 'accounts/signup.html', {'form' : form, 'status': 'diff'})
        #위의 경우가 아니면 db에 입력받은 내용 저장            
        UserModel.objects.create(
                username=data['username'],
                password=data['password'],
            ).save()
        return render(request,'searchapp/index.html',{'obj':obj,'status':'login'})
        #return render(request, 'searchapp/index.html', {'status': 'login'})
    else:
        return render(request,'accounts/signup.html', {'form':form})