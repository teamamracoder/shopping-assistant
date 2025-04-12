from django import forms
from ..models import ServiceModel


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        # fields = ['service_type', 'service_provider', 'services_charge', 'description']
        fields = ['service_type', 'service_provider', 'services_charge', 'description', 'is_active']
