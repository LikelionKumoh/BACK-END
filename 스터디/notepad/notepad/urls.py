from django.contrib import admin
from django.urls import path, include
from main import views
from accounts import views as accounts_views
from memo import views as memo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('login/',accounts_views.login,name="login"),
    path('logout/',accounts_views.logout, name="logout"),
    path('new/',memo_views.formcreate,name="new"),
    path('detail/<int:memo_id>',memo_views.detail,name='detail'),
    path('accounts/',include('allauth.urls')),
]
