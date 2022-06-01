from django.urls import path, include
from . import views


app_name = 'note'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:memo_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]