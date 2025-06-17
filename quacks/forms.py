from django import forms
from .models import Quack

class QuackForm(forms.ModelForm):
    class Meta:
        model = Quack
        fields = ['body']

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.fields['body'].widget.attrs.update({
            'placeholder': 'O que está acontecendo? Solte seu Quack',
            'class': 'input mb-4',
            'style': 'min-height: 8rem; resize: none',
            'maxlength': '255',
            'required': True 
        })

        self.fields['body'].label = ""