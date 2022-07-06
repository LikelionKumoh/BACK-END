from django.urls import path
from .views import home,search, CreateView, LoginView, signout

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('<str:choice>/<str:text>', search),
    path('signup/', CreateView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', signout, name='signout')
]