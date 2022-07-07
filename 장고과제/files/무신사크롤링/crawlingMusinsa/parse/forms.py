from tkinter import Label
from django import forms

class Searchform(forms.Form):
    search = forms.CharField(label='상품을 검색해주세요..', max_length=100)
