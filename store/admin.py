from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'address', 'created_at', 'is_archived')

admin.site.register(Store, StoreAdmin)
