from django import forms
from .models import Product

class SearchForm(forms.Form):
    search = forms.CharField(label='search for ...', max_length=100)
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'