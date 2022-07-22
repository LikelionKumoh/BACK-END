import json
from django.http import HttpResponse
import bcrypt
import requests
from django.shortcuts import render,redirect
from django.http            import JsonResponse  
from django.views           import View          
from django.contrib import messages                                                                                                  
from parse.models          import Accounts 

MINIMUM_PASSWORD_LENGTH = 8  


class SignUpView(View):
        def post(self, request):
            print(request.body)
            data =json.loads(request.body)
            if Accounts.objects.filter(username=data['username']).exists():
                context = {
                    "result": "중복입니다..."
                }
                return HttpResponse(json.dumps(context),content_type="application/json")
            else:
                if data['password1']==data['password2']:
                    Accounts.objects.create(username=data['username'],password=data['password1'],email=data['email'])
                    login_stat = True if request.session.get('user') else False
                    context = {"login_stat": login_stat}
                    return render(request, 'home/home.html', context)
        def get(self, request):
            return render(request, 'signup.html')

class LoginView(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)

        if Accounts.objects.filter(username = data['username'], password = data['password']).exists():
            user = Accounts.objects.get(username=data['username'])
            request.session['user'] = user.id
            login_stat = True if request.session.get('user') else False
            context = {"login_stat": login_stat}
            return render(request, 'home/home.html', context)
        else:
            context = {
                "result": "정보가 틀렸습니다."
            }
            return HttpResponse(json.dumps(context),content_type="application/json")

    def get(self, request):
        return render(request, 'login.html')

def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('home')