from django.contrib import admin
from django.urls import path, include
import main.urls, account.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main.urls)),
    path('account/', include(account.urls)), 
    # path('notepad/', include(notepad.urls)),
]
