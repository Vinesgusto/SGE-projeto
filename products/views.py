from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from django.urls import reverse_lazy
from categories.models import Categories
from brands.models import Brand
from .forms import ProductForm
from . import models
from django.db.models import Sum

class ProductListView(ListView): 
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    total_quantity = Sum('quantity')

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        serie_number = self.request.GET.get('serie_number')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__istartswith=serie_number)

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_products_metrics()
        context['categories'] = Categories.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    
    

class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
# Create your views here.

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'

class ProductUpadateView(UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
 
    