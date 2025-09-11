from django import forms
from .models import Categories  

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome da Categoria',
            'description': 'Descrição',
        }