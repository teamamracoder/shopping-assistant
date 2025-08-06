from django import forms
from ..models import UserModel
from constants import Gender, Role 

class ManageUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'email', 'dob', 'gender', 'phone',
            'address', 'country', 'location', 'city', 'district', 'state', 'pincode', 'roles'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode', 'maxlength': 6}),
            'roles': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'role'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override gender and roles choices using enums
        self.fields['gender'].choices = [(g.value, g.name) for g in Gender]
        self.fields['roles'].choices = [(r.value, r.name) for r in Role]
        self.fields['city'].label = 'City/Village:'
        self.fields['country'].initial = 'India'