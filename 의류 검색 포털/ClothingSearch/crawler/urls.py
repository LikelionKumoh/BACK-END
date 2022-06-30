from django.urls import path

from crawler import views

urlpatterns = [
    path('', view=views.clothing_data, name='clothing_data')
]