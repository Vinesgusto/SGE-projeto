
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('brands.urls')),
    path('', include('categories.url')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
   
]
