from django import forms
from ..models import ServiceTypeModel

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceTypeModel
        fields = ['service_name', 'is_active', 'created_by', 'updated_by']
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter service type name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-select'}),
            'updated_by': forms.Select(attrs={'class': 'form-select'}),
        }
