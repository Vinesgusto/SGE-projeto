from django.db import models
from suppliers.models import Suppliers
from products.models import Product
from django import forms

class Inflow(models.Model):
   supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name='inflows')
   product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
   quantity = models.IntegerField()
   description = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   widgets = {
            created_at: forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

   

   class Meta:
       ordering = ['-created_at'] 

   def __str__(self):
       return str(self.product)       
 

# Create your models here. 
