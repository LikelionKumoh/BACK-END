from socket import fromshare
from django import forms
from .models import Memo

class MemoForm(forms.Form):
    #내가 입력받고자 하는 값들
    body = forms.CharField(widget=forms.Textarea)
