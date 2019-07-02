from django import forms
from materials.models import Ad, Complaint


class AdVendaForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['price', 'address', 'latitude', 'longitude']
        widgets = {'latitude': forms.HiddenInput(
        ), 'longitude': forms.HiddenInput()}


class AdEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['address', 'latitude', 'longitude']
        widgets = {'latitude': forms.HiddenInput(
        ), 'longitude': forms.HiddenInput()}


class AdDoacaoForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['address', 'latitude', 'longitude']
        widgets = {'latitude': forms.HiddenInput(
        ), 'longitude': forms.HiddenInput()}


class AdComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['message', 'complaint_type']
