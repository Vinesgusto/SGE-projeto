from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models
from .forms import SupplierForm




class SupplierListView(ListView):
    model = models.Suppliers
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
class SupplierCreateView(CreateView):
    model = models.Suppliers
    template_name = 'supplier_form.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDetailView(DetailView):
    model = models.Suppliers
    template_name = 'supplier_detail.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = models.Suppliers
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = models.Suppliers
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')

