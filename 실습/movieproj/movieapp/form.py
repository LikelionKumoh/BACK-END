from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search For Movies..',max_length=100)

    def __init__(self,*args,**kwargs):
        super(SearchForm, self).__init__(*args,**kwargs)

        self.fields['search'].widget.attrs = {
            'class':'form-control',
            'placeholder':"영화 제목을 검색하세요.",
            'rows' : 20
        }
        