from django import forms
from ..models import StoreModel


class StoreForm(forms.ModelForm):
    class Meta:
        model = StoreModel
        exclude = ['created_by', 'updated_by', 'created_at', 'updated_at']
        widgets = {
            'owner': forms.Select(attrs={'class': 'form-select'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control'}),
            'store_category': forms.Select(attrs={'class': 'form-select'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'alternate_contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'alternate_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'open_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'close_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'street_or_road': forms.TextInput(attrs={'class': 'form-control'}),
            'village_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control'}),
            'store_image_urls': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_store_image_urls(self):
        data = self.cleaned_data.get('store_image_urls', [])
        # If entered as newline-separated text in textarea
        if isinstance(data, str):
            urls = [url.strip() for url in data.splitlines() if url.strip()]
            return urls
        return data
