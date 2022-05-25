from django.urls import path, include
from kit import views

urlpatterns = [
    path('', views.home, name="home"),
    path('kit/', views.kit, name="kit"),
    path('likelion/', views.likelion, name="likelion"),
    path('kit/computer/', views.computer, name="computer"),
    path('likelion/backEnd/', views.backEnd, name="backEnd"),
    path('likelion/frontEnd/', views.frontEnd, name="frontEnd"),
    path('likelion/pmDesign/', views.pmDesign, name="pmDesign"),
    path('likelion/backEnd/mypage/', views.mypage, name="mypage"),
    
]
