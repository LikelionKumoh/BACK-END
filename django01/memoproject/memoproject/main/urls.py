from django.urls import path, include
from main import views
import userapp.urls, notepad.urls


urlpatterns = [
    path('', views.main, name="main"),
    path('accounts/', include(userapp.urls)),
    path('notepad/', include(notepad.urls))
] 
    
