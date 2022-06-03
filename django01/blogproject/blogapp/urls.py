from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('', views.home, name="home"),

    #html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    #django modelform을 이용해 블로그 객체 만들기
    path('modelcreate/', views.modelcreate, name='modelcreate'),

    # 상세 페이지
    path('detail/<int:post_id>', views.detail, name='detail'),

    # 댓글 저장
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),
] 
