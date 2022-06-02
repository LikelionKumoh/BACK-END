from django.contrib import admin
from django.urls import path, include
from noteapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login/',accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('postcreate/',views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'), 
    path('accounts/', include('allauth.urls')),
    ]
