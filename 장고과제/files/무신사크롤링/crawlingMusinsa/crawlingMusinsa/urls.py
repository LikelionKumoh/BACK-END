
from django.contrib import admin
from django.urls import path
from main import views
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',account_views.login,name='login'),
    path('logout/',account_views.logout,name='logout'),
    path('signup/',account_views.signup,name='signup'),
]
