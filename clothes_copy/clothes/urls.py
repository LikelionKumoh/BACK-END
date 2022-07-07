
from django.contrib import admin
from django.urls import path
from clothesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('/search',views.search,name='search'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
