from django import forms
from materials.models import Ad


class AdVendaForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['price']
