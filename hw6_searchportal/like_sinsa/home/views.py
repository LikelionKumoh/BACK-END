from django.shortcuts import render, redirect
from django.http import HttpResponse

from .crawltest import get_data
from .models import Goods, User
from django.views import View
from django.contrib import messages
import json


# Create your views here.


def home(request):
    login_stat = True if request.session.get('user') else False
    context = {'login_stat': login_stat}
    return render(request, 'home/home.html', context)


def search(request, choice, text):

    user_id = request.session.get('user')

    if user_id:
        Goods.objects.all().delete()
        get_data(text, choice)
        goods_list = Goods.objects.all()
        context = {"goods_list": goods_list}
        return render(request, 'home/show.html', context)
    else:
        messages.info(request, '로그인을 해주세요!')
        return render(request, 'home/login.html')


def signout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('home:home')


class CreateView(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        if User.objects.filter(user_id = data['user_id']).exists():
            context = {
                "result": "이미 존재하는 아이디입니다."
            }
            return HttpResponse(json.dumps(context),content_type="application/json")

        else:
            User.objects.create(user_id = data['user_id'], password = data['password'])
            messages.info(request, '회원가입 성공!')
            login_stat = True if request.session.get('user') else False
            context = {"login_stat": login_stat}
            return render(request, 'home/home.html', context)

    def get(self, request):
        return render(request, 'home/register.html')


class LoginView(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)

        if User.objects.filter(user_id = data['user_id'], password = data['password']).exists():
            user = User.objects.get(user_id=data['user_id'])
            request.session['user'] = user.id
            messages.info(request, '로그인 성공!')
            login_stat = True if request.session.get('user') else False
            context = {"login_stat": login_stat}
            print(context)
            return render(request, 'home/home.html', context)
        else:
            context = {
                "result": "id 또는 pw가 틀렸습니다"
            }
            return HttpResponse(json.dumps(context),content_type="application/json")

    def get(self, request):
        return render(request, 'home/login.html')