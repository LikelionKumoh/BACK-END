from django import forms
from .models import Memo


class MemoModelForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']

