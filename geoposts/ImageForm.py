from django import forms
from .models import Image

class GeoImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)