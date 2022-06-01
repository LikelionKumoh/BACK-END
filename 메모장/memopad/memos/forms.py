from django import forms

class MemoForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)