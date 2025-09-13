from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CategoryForm
from . import models



class CategoryListView(ListView):
    model = models.Categories
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    

    def get_queryset(self):
        quaryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            quaryset = quaryset.filter(name__icontains=name)
        return quaryset

class CategoryCreateView(CreateView):
    model = models.Categories
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDetailView(DetailView):
    model = models.Categories
    template_name = 'category_detail.html'
    

class CategoryUpadateView(UpdateView):
    model = models.Categories
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

class CategoryDeleteView(DeleteView):
    model = models.Categories
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
