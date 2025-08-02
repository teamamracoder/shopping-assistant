from django import forms
from ..models import StoreModel

class ManageStoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['store_category'].empty_label = "Select"

    class Meta:
        model = StoreModel
        # exclude = ['created_at', 'updated_at', 'created_by', 'updated_by']
        fields = [
            'store_name', 'registration_no', 'gst_no', 'contact_no', 'email',
            'open_time', 'close_time', 'pin_code', 'owner', 'store_category'
        ]

        widgets = {
            'store_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_store_name',
                'placeholder': 'Enter store name'
            }),
            'registration_no': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_registration_no',
                'placeholder': 'Enter registration number'
            }),
            'gst_no': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_gst_no',
                'placeholder': 'Enter GST number'
            }),
            'contact_no': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_contact_no',
                'placeholder': 'Enter contact number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'id_email',
                'placeholder': 'Enter email'
            }),
            'store_category': forms.Select(attrs={
                "class": "form-control",
                'id': 'id_store_category'
            }),
             'open_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'id': 'id_open_time',
                'class': 'form-control'
            }),
            'close_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'id': 'id_close_time',
                'class': 'form-control'
            }),
            'pin_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_pin_code',
                'placeholder': 'Enter pin code'
            }),
            # 'is_active': forms.CheckboxInput(attrs={
            #     'class': 'form-check-input',
            # }),
            'owner': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_owner',
            }),
        }

        labels = {
            'store_name': "Store Name",
            'registration_no': "Registration No",
            'gst_no': "GST No",
            'contact_no': "Contact Number",
            'email': "Email",
            'store_category': "Store Category",
            'open_time': "Open Time",
            'close_time': "Close Time",
            'pin_code': "Pincode",
            'owner_id': "Owner",
        }
