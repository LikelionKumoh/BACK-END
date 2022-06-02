from django import forms
from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields='__all__'

class PostForm(forms.Form):
    body=forms.CharField(widget=forms.Textarea)
