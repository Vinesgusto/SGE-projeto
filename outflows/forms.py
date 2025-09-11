from django import forms
from .models import Outflow

class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'product': 'Produto', 
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if not product:
            raise forms.ValidationError('Selecione um produto.')

        if not quantity:
            raise forms.ValidationError('Informe a quantidade.')

        if quantity > product.quantity:
            raise forms.ValidationError(
                f'Quantidade insuficiente do produto {product.title} em estoque. Estoque atual: {product.quantity}.'
            )

        return quantity
    
