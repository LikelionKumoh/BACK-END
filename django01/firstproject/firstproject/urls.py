
from django.contrib import admin
from django.urls import path, include
import board.urls, product.urls, kit.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include(board.urls)),
    path('product/', include(product.urls)),
    path('kit/', include(kit.urls)),
]
