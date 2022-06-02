from django.contrib import admin
from django.urls import path, include
from main import views
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('create/', views.create,name='create'),

    path('detail/<int:Note_id>',views.detail, name='detail'),

    path('login/', accounts_views.login,name='login'),
    path('logout/', accounts_views.logout,name='logout'),
    path('google/', include('allauth.urls')),
    path('naver/', include('allauth.urls')),
    path('kakao/', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
]
