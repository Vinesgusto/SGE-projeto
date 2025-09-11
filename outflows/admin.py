from django.contrib import admin

from . import models

class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at')
    search_fields = ('product__title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(models.Outflow, OutflowAdmin)

# Register your models here.
