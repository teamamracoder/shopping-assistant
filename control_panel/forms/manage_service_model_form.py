from django import forms
from ..models import ServiceModel


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ['service_type', 'service_provider', 'services_charge', 'description', 'is_active']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control', 'name': 'service_type'}),
            'service_provider': forms.Select(attrs={'class': 'form-control', 'name': 'service_provider'}),
            'services_charge': forms.NumberInput(attrs={'class': 'form-control', 'name': 'services_charge'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'name': 'description','rows':1}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'name': 'is_active'}),
        }