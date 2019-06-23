from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Address


class ProfileForm(UserCreationForm):
    birth = forms.DateField(
        required=False, help_text='Formato: YYYY-MM-DD')
    CPF = forms.CharField(required=False)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'username', 'email', 'birth',
                  'CPF', 'password1', 'password2')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'complement',
                  'district', 'city', 'CEP', ]
