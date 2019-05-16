from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):
    birth = forms.DateField(
        required=False, help_text='Formato: YYYY-MM-DD')
    CPF = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'birth',
                  'CPF', 'password1', 'password2')
