from django.shortcuts import render, redirect
from .models import User

def signup(request):
    if request.method == 'POST':
        res_data = {}
        if request.POST['password'] == request.POST['passwordcheck']:
            user = User.objects.create(
                username=request.POST['username'],
                password=request.POST['password'],
                name=request.POST['name'],
            )
            request.session['user'] = user.id
            res_data['success'] = '회원가입 성공, 쇼핑 목록을 조회하려면 로그인하세요.'
            return render(request, 'account/login.html', res_data)
        else:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
            return render(request, 'account/signup.html', res_data)
    return render(request, 'account/signup.html')
     
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        res_data = {}
        
        # 모든 필드를 채우지 않았을 경우
        if not (username and password):
            res_data['error'] = '모든 값을 입력해 주세요.'
        else:
            user = User.objects.get(username=username)
            if password == user.password:
                request.session['user'] = user.id
                return redirect('/')

            else:
                res_data['error'] = '잘못된 비밀번호 입니다.'
                return render(request, 'account/login.html', res_data)
        return render(request, 'account/login.html', res_data)

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
