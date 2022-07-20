from django.contrib import admin
from django.urls import path
from crawler import views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', account_views.signup, name='signup'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
]
