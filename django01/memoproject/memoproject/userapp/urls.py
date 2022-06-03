from django.urls import path, include
from userapp import views
from django.conf import settings


urlpatterns = [
    path('login', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('', include('allauth.urls')),
] 
    