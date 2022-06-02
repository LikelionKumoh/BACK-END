
from django.contrib import admin
from django.urls import path,include
from noteapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('newmemo',views.newmemo,name='newmemo'),
    path('detail/<int:memo_id>',views.detail,name='detail'),

    path('login/',accounts_views.login,name='login'),
    path('logout/',accounts_views.logout,name='logout'),

    path('accounts/', include('allauth.urls')),
    # path('accounts/kakao/login/callback/',accounts_views.kakaologin,name = 'kakaologin'),

]
