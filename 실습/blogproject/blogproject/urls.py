from unicodedata import name
from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),

    path('new/',views.new,name="new"),
    path('create/',views.create,name="create"),

    path('create/', views.formcreate, name='formcreate'),
    path('formcreate/', views.formcreate, name='formcreate'),
    path('modelformcreate/',views.modelformcreate, name='modelformcreate'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
