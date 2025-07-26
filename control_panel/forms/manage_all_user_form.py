from django import forms
from ..models import UserModel

from django import forms
from ..models import UserModel
from constants import Gender, Role  # These should be Python Enums

from django import forms
from ..models import UserModel
from constants import Gender, Role  # Enums

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
            'pincode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'}),
            'roles': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'role'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override gender and roles choices using enums
        self.fields['gender'].choices = [(g.value, g.name) for g in Gender]
        self.fields['roles'].choices = [(r.value, r.name) for r in Role]





















































# class ManageUserForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})
#     )
#     last_name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
#     )
#     dob = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
#     )
#     gender = forms.ChoiceField(
#         choices=[(g.value, g.name) for g in Gender],
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     phone = forms.CharField(
#         max_length=15,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'})
#     )
#     address = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'})
#     )
#     country = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control','palceholder': 'Enter your country'})
#     )
#     location = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'})
#     )
#     city = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
#     )
#     district = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'})
#     )
#     state = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'})
#     )
#     pincode = forms.CharField(
#         max_length=6,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'})
#     )
#     roles = forms.MultipleChoiceField(
#     choices=[(role.value, role.name) for role in Role],
#     required=False,
#     widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'role'})
# )