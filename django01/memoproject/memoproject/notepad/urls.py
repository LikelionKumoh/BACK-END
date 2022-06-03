from django.urls import path, include
from notepad import views
import userapp.urls


urlpatterns = [
    path('create/', views.create, name="create"),
    path('detail/<int:memo_id>', views.detail, name="detail"),
] 
    