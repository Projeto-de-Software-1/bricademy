from django import forms
from.models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'author', 'ISBN', 'publishing_company',
                  'publication_date', 'conservation', 'category', 'subject']
