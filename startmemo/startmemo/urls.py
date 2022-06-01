
from django.contrib import admin
from django.urls import path, include
from memoapp import views
from accounts import views as accounts_views
from django.conf import settings
# from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    
    path('detail/<int:memo_id>', views.detail, name='detail'),
    # path('new_comment/<int:memo_id>', views.new_comment, name='new_comment'),
    
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    
    path('accounts/', include('allauth.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)