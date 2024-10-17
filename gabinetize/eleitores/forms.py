from django import forms
from .models import Eleitor

class EleitorForm(forms.ModelForm):
    class Meta:
        model = Eleitor
        fields = ['nome', 'endereco', 'telefone', 'secao', 'zona']
