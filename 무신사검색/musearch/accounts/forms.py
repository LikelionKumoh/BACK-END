from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserModel
        fields='__all__'
        
class CreateUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    checkpassword=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserModel
        fields='__all__'        