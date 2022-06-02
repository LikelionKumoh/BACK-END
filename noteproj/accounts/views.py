from django.shortcuts import render,redirect
from django.contrib import auth #이미 있는 회원인지를 확인할 수 있다. 
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    #POST 요청: 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd= request.POST['password']
        user = auth.authenticate(request,username=userid,password=pwd) #해당 회원이 있으면 회원(user) 객체를, 없으면 none을 반환
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')
    #GET요청: login.html 띄우기
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def kakaologin(request):
        try:
            if request.user.is_authenticated:
                raise SocialLoginException("User already logged in")
            client_id = 'ecf85902822816e7dfe4fa23d31671f2'
            redirect_uri = "http://localhost:8000/accounts/kakao/login/callback/"

            return redirect(
                f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
            )
        except KakaoException as error:
            messages.error(request, error)
            return redirect("core:home")
        except SocialLoginException as error:
            messages.error(request, error)
            return redirect("core:home")