from django.contrib import admin
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Goods , GoodsAdmin)

# Register your models here.
