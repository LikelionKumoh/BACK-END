
from django.contrib import admin
from django.urls import path, include
import blogapp.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blogapp.urls)),


] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
