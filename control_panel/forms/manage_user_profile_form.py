from django import forms
from ..models import UserModel
from constants.enums import Gender, Role

class ManageUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'dob', 'gender',
            'address', 'country', 'city', 'district', 'state', 'location',
            'pincode', 'designation', 'bio'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
                'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
                'id': 'last_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'id': 'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'id': 'phone'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'dob'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',
                'id': 'gender'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 3,
                'id': 'address'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your country',
                'id': 'country'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your city',
                'id': 'city'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your district',
                'id': 'district'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your state',
                'id': 'state'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location',
                'id': 'location'
            }),
            'pincode': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your pincode',
                'id': 'pincode'
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your designation',
                'id': 'designation'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about yourself',
                'rows': 4,
                'id': 'bio'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'Select Gender')] + [(g.value, g.name.title()) for g in Gender]