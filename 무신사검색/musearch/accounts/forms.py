from django import forms

class UserForm(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.CharField(max_length=12,widget=forms.PasswordInput,required=True)

class CreateUserForm(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.CharField(max_length=12,widget=forms.PasswordInput,required=True)
    check_Password = forms.CharField(max_length=12,widget=forms.PasswordInput,required=True)
