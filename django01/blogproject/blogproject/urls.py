
from django.contrib import admin
from django.urls import path, include
import blogapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blogapp.urls)),


]


