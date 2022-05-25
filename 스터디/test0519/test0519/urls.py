from django.contrib import admin
from django.urls import path
from home import views as hviews
from likelion import views as lviews
from backend import views as bviews
from computer import views as cviews
from kit import views as kviews
from frontend import views as fviews
from pmdisign import views as pviews
from mypage import views as mviews




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hviews.home),
    path('frontend/',fviews.home),
    path('backend/',bviews.home),
    path('pmdisign/',pviews.home),
    path('kit/',kviews.home),
    path('computer/',cviews.home),
    path('likelion/',lviews.home),
    path('mypage/',mviews.home),
]
