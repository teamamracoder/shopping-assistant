from django import forms
from ..models import ServiceBookingModel

class ManageServiceBookingForm(forms.ModelForm):
    booking_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        input_formats=['%Y-%m-%dT%H:%M'],  # HTML datetime-local format
    )

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
            'created_by': forms.HiddenInput(),
            'updated_by': forms.HiddenInput(),
        }