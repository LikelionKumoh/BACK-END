from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.main, name="main"),
    path('create/', views.create, name="create"),
    path('detail/<int:memo_id>', views.detail, name="detail"),
] 
    