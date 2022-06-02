from django.urls import path, include
from account import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
] 
    