from .models import Notepad
from django import forms

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notepad
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "메모를 입력해주세요",
            'rows': 20,
            'cols' : 100
        }