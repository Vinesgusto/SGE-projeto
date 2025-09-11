from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models
from .forms import OutflowForm





class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(name__title__icontains=product)
        return queryset
    
class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_form.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')

class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    success_url = reverse_lazy('outflow_list')



# Create your views here.
