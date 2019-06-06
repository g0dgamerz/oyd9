from django import forms
from .models import journal

class journalForm(forms.ModelForm):
    class Meta:
        model=journal
        fields="__all__"