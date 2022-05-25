from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),
    path('second/',views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls'))
]
