from django.shortcuts import render
from django.db import models
from products.models import Product

total_quantity = Product.objects.aggregate(models.Sum('quantity'))['quantity__sum'] or 0
stock_cost = Product.objects.aggregate(total_cost_price=models.Sum(models.F('quantity') * models.F('cost_price')))['total_cost_price'] or 0
stock_value = Product.objects.aggregate(total_sale_price=models.Sum(models.F('quantity') * models.F('selling_price')))['total_sale_price'] or 0
stock_profit = stock_value - stock_cost

def home(request):
    product_metrics = {
        'total_quantity': total_quantity,
        'total_cost_price': stock_cost,
        'total_selling_price': stock_value,
        'total_profit': stock_profit,
    }


    context = {
        'product_metrics': product_metrics
        }
    return render(request, 'home.html', context)


    