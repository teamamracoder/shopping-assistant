
# from django import forms
# from django.core.exceptions import ValidationError
# from ..models import StoreModel, StoreCategoryModel
# import re

from django import forms
from django.core.exceptions import ValidationError
from ..models import StoreModel, StoreCategoryModel
import re


# class ManageStoreForm(forms.ModelForm):
#     store_category = forms.ModelChoiceField(
#         queryset=StoreCategoryModel.objects.filter(is_active=True),
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         empty_label="Select a category"
#     )

#     contact_no = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'})
#     )

#     email = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
#     )

#     class Meta:
#         model = StoreModel
#         fields = [
#             'store_name', 'registration_no', 'gst_no', 'store_category',
#             'contact_no', 'alternate_contact_no', 'email', 'alternate_email',
#             'open_time', 'close_time', 'address', 'location', 'street_or_road',
#             'village_or_city', 'district', 'state', 'pin_code',
#             'store_image_urls', 'is_active'
#         ]

#         common_text_input = lambda placeholder='': forms.TextInput(attrs={
#             'class': 'form-control', 'placeholder': placeholder
#         })

#         widgets = {
#             'store_name': common_text_input('Enter store name'),
#             'registration_no': common_text_input('Enter registration number'),
#             'gst_no': common_text_input('Enter GST number'),
#             'alternate_contact_no': common_text_input('Enter alternate contact number'),
#             'alternate_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter alternate email'}),
#             'open_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#             'close_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'}),
#             'location': common_text_input('Enter location'),
#             'street_or_road': common_text_input('Enter street or road name'),
#             'village_or_city': common_text_input('Enter village or city'),
#             'district': common_text_input('Enter district'),
#             'state': common_text_input('Enter state'),
#             'pin_code': common_text_input('Enter pin code'),
#         }

#     def validate_phone(self, number, field_name):
#         if number and not re.match(r'^\d{10}$', number):
#             raise ValidationError(f"Enter a valid 10-digit {field_name}.")
#         return number

#     def validate_email(self, email, field_name):
#         if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
#             raise ValidationError(f"Enter a valid {field_name}.")
#         return email

#     def clean_contact_no(self):
#         return self.validate_phone(self.cleaned_data.get('contact_no'), 'contact number')


#     def clean_alternate_contact_no(self):
#         return self.validate_phone(self.cleaned_data.get('alternate_contact_no'), 'alternate contact number')

#     def clean_email(self):
#         return self.validate_email(self.cleaned_data.get('email'), 'email address')

#     def clean_alternate_email(self):
#         return self.validate_email(self.cleaned_data.get('alternate_email'), 'alternate email address')

contact_no = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'})
    )

email = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )


#     def clean_pin_code(self):
#         pin_code = self.cleaned_data.get('pin_code')
#         if pin_code and not re.match(r'^\d{6}$', pin_code):
#             raise ValidationError("Enter a valid 6-digit PIN code.")
#         return pin_code

#     def clean(self):
#         cleaned_data = super().clean()
#         open_time = cleaned_data.get("open_time")
#         close_time = cleaned_data.get("close_time")
#         if open_time and close_time and close_time <= open_time:
#             raise ValidationError("Closing time must be after opening time.")



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

        fields = [
            'store_name', 'registration_no', 'gst_no', 'store_category',
            'contact_no', 'alternate_contact_no', 'email', 'alternate_email',
            'open_time', 'close_time', 'address', 'location', 'street_or_road',
            'village_or_city', 'district', 'state', 'pin_code',
            'store_image_urls', 'is_active'
        ]

        common_text_input = lambda placeholder='': forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': placeholder
        })

        widgets = {
            'store_name': common_text_input('Enter store name'),
            'registration_no': common_text_input('Enter registration number'),
            'gst_no': common_text_input('Enter GST number'),
            'alternate_contact_no': common_text_input('Enter alternate contact number'),
            'alternate_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter alternate email'}),
            'open_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'close_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'}),
            'location': common_text_input('Enter location'),
            'street_or_road': common_text_input('Enter street or road name'),
            'village_or_city': common_text_input('Enter village or city'),
            'district': common_text_input('Enter district'),
            'state': common_text_input('Enter state'),
            'pin_code': common_text_input('Enter pin code'),
        }

    def validate_phone(self, number, field_name):
        if number and not re.match(r'^\d{10}$', number):
            raise ValidationError(f"Enter a valid 10-digit {field_name}.")
        return number

    def validate_email(self, email, field_name):
        if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError(f"Enter a valid {field_name}.")
        return email

    def clean_contact_no(self):
        return self.validate_phone(self.cleaned_data.get('contact_no'), 'contact number')

    def clean_alternate_contact_no(self):
        return self.validate_phone(self.cleaned_data.get('alternate_contact_no'), 'alternate contact number')

    def clean_email(self):
        return self.validate_email(self.cleaned_data.get('email'), 'email address')

    def clean_alternate_email(self):
        return self.validate_email(self.cleaned_data.get('alternate_email'), 'alternate email address')

    def clean_pin_code(self):
        pin_code = self.cleaned_data.get('pin_code')
        if pin_code and not re.match(r'^\d{6}$', pin_code):
            raise ValidationError("Enter a valid 6-digit PIN code.")
        return pin_code

    def clean(self):
        cleaned_data = super().clean()
        open_time = cleaned_data.get("open_time")
        close_time = cleaned_data.get("close_time")
        if open_time and close_time and close_time <= open_time:
            raise ValidationError("Closing time must be after opening time.")

