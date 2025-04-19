from django import forms
from django.core.exceptions import ValidationError
from ..models import StoreModel, StoreCategoryModel
import re
from django import forms
from ..models import StoreModel  # Update this if your model name or import path differs


class ManageStoreForm(forms.ModelForm):
    class Meta:
        model = StoreModel

        fields = '__all__'

        widgets = {
            'store_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter store name',
                'id': 'id_store_name',
                'name': 'store_name',
            }),
            'registration_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter registration number',
                'id': 'id_registration_no',
                'name': 'registration_no',
            }),
            'gst_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter GST number',
                'id': 'id_gst_no',
                'name': 'gst_no',
            }),
            'contact_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number',
                'id': 'id_contact_no',
                'name': 'contact_no',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',
                'id': 'id_email',
                'name': 'email',
            }),
            'alternate_contact_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter alternate contact',
                'id': 'id_alternate_contact_no',
                'name': 'alternate_contact_no',
            }),
            'alternate_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter alternate email',
                'id': 'id_alternate_email',
                'name': 'alternate_email',
            }),
            'open_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'id': 'id_open_time',
                'name': 'open_time',
            }),
            'close_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'id': 'id_close_time',
                'name': 'close_time',
            }),
            'store_category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_store_category',
                'name': 'store_category',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location',
                'id': 'id_location',
                'name': 'location',
            }),
            'street_or_road': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter street/road',
                'id': 'id_street_or_road',
                'name': 'street_or_road',
            }),
            'village_or_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter village/city',
                'id': 'id_village_or_city',
                'name': 'village_or_city',
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter district',
                'id': 'id_district',
                'name': 'district',
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter state',
                'id': 'id_state',
                'name': 'state',
            }),
            'pin_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pin code',
                'id': 'id_pin_code',
                'name': 'pin_code',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full address',
                'rows': 2,
                'id': 'id_address',
                'name': 'address',
            }),
        }   