from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'supplier',
                   'description', 'serie_number', 'cost_price', 'selling_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),

        }

        labels = {'title': 'Produto',
                  'category': 'Categoria',
                  'brand': 'Marca',
                  'description': 'Descrição',
                  'serie_number': 'Número de Série',
                  'cost_price': 'Preço de Custo',
                  'selling_price': 'Preço de Venda',
                  'supplier': 'Fornecedor'
                  }


def clean_preco(self):
    preco = self.cleaned_data['cost_price', 'selling_price']
    preco = preco.replace(".", "").replace(",", ".")
    return float(preco)
