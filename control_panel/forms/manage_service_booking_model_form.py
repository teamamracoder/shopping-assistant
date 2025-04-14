from django import forms
from ..models import ServiceBookingModel

class ManageServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBookingModel
        fields = [
            'service',
            'service_provider',
            'user',
            'booking_charge',
            'booking_time',
            'created_by',
            'updated_by',
        ]
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'service_provider': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'booking_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'booking_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'created_by': forms.HiddenInput(),
            'updated_by': forms.HiddenInput(),
        }
