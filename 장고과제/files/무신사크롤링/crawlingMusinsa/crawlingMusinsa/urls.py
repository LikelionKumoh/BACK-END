
from django.contrib import admin
from django.urls import path
from parse import views
from accounts.views import SignUpView, logout, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
]
