from django.contrib import admin
from . import models  

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
   


admin.site.register(models.Categories, categoriesAdmin)


# Register your models here.
