from email import message
from sqlite3 import Cursor
from django.shortcuts import redirect, render
from .forms import ProductModelForm
from .models import Product
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def login(request):
    con = mysql.connector.connect(host='localHost', user='root', password='qwqw1212', port=3306, use_unicode=True, charset='utf8', auth_plugin='mysql_native_password', database="clothes")
    cursor = con.cursor()
    con2 = mysql.connector.connect(host='localHost', user='root', password='qwqw1212', port=3306, use_unicode=True, charset='utf8', auth_plugin='mysql_native_password', database="clothes")
    cursor2 = con2.cursor()
    sqlcommand = "select email from clothesapp_user"
    sqlcommand2 = "select password from clothesapp_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        i = 0
        k = len(res)
        while i < k:
            if res[i] == email and res2[i] == password:
                return render(request, 'index.html', {'email':email})
            i += 1
        messages.info(request, "Check name OR password")
        return redirect('login')
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        user = User()
        
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.repassword = request.POST['repassword']
        
        if user.password != user.repassword:
            return redirect('register')
        elif user.fname == "" or user.password == "":
            messages.info(request, "some feild are empty")
            return redirect('register')
        else:
            user.save()
    return render(request, 'register.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        products = Product.objects.filter(name__contains=searched) | Product.objects.filter(brand__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'products':products})
    else:
        return render(request, 'search.html', {})