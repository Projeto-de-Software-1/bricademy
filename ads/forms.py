from django import forms
from materials.models import Ad


class AdVendaForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['price', 'address', 'latitude', 'longitude']
        widgets = {'latitude': forms.HiddenInput(
        ), 'longitude': forms.HiddenInput()}
