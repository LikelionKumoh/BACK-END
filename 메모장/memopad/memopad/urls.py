from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from memos import views as memos_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),

    path('write/', memos_views.write, name='write'),
    path('detail/<int:memo_id>', memos_views.detail, name='detail'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]
