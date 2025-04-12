from django import forms
from ..models import StoreModel, StoreCategoryModel

class ManageStoreForm(forms.ModelForm):
    store_category = forms.ModelChoiceField(
        queryset=StoreCategoryModel.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select a category"
    )

    contact_no = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
    required=False
)

    email = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
    required=False
)


    class Meta:
        model = StoreModel
        fields = [
            'store_name', 'registration_no', 'gst_no', 'store_category',
            'contact_no', 'alternate_contact_no', 'email', 'alternate_email',
            'open_time', 'close_time', 'address', 'location', 'street_or_road',
            'village_or_city', 'district', 'state', 'pin_code',
            'store_image_urls', 'is_active'
        ]
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control'}),
            'alternate_contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter alternate contact number'}),
            'alternate_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter alternate email'}),
            'open_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'close_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
        'placeholder': 'Enter full address'}),
            'location': forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter location'}),
            'street_or_road': forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter street or road name'}),
            'village_or_city': forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter village or city'}),
            'district': forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter district'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter state'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Enter pin code'}),
            
        }

