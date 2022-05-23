from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.board, name="home"),
    path('first/', views.boardfirst, name='about')
]
