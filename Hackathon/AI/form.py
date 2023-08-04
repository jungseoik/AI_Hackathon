
from django import forms
from .models import InputText

class InputTextForm(forms.ModelForm):
    class Meta:
        model = InputText
        fields = ['text']