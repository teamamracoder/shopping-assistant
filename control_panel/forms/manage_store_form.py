from django import forms
from ..models import StoreModel, StoreCategoryModel

class ManageStoreForm(forms.ModelForm):
    # Define the store_category field as a ModelChoiceField
    store_category = forms.ModelChoiceField(
        queryset=StoreCategoryModel.objects.filter(is_active=True),  # Fetch only active categories
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select a category"  # Optional: Custom label for the empty choice
    )
    # Define other fields as needed
    contact_no = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter contact numbers separated by commas'}),
        required=False
    )
    email = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter emails separated by commas'}),
        required=False
    )
    store_image_urls = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter image URLs separated by commas'}),
        required=False
    )

    class Meta:
        model = StoreModel
        fields = [
       'store_name', 'registration_no', 'gst_no', 'store_category', 
            'contact_no', 'email', 'open_time', 'close_time', 'address', 'location',
            'street_or_road', 'village_or_city', 'district', 'state', 'pin_code', 
            'store_image_urls', 'is_active'
        ]
        widgets = {
          
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter store name'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter registration number'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GST number'}),
            'open_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'close_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'street_or_road': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter street or road'}),
            'village_or_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter village or city'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pin code'}),
            'is_active': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
          
        }

    def clean_contact_no(self):
        contact_no = self.cleaned_data.get('contact_no')
        return [num.strip() for num in contact_no.split(',')] if contact_no else []

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return [mail.strip() for mail in email.split(',')] if email else []

    def clean_store_image_urls(self):
        store_image_urls = self.cleaned_data.get('store_image_urls')
        return [url.strip() for url in store_image_urls.split(',')] if store_image_urls else []
