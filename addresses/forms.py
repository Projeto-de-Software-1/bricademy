from django import forms
from django.contrib.auth.models import User
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'complement',
                  'district', 'city', 'CEP', ]
