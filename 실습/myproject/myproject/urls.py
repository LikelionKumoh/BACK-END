#url을 관리해주고 등록하는 파일(스프링 controller와 동일)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
