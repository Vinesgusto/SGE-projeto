from django.contrib import admin
from . import models

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    

admin.site.register(models.Suppliers, SupplierAdmin)
# Register your models here.
