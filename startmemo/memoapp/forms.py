
from django import forms
from .models import Memo, Comment
    
class MemogModelForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'
        # fields = ['title', 'body']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']