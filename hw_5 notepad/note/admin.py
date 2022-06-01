from django.contrib import admin
from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Memo, MemoAdmin)
