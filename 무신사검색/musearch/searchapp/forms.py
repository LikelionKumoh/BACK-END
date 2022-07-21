from django import forms

class SearchForm(forms.Form):
    search=forms.CharField(label='검색', max_length=30)
