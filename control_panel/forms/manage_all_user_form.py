from django import forms
from ..models import UserModel
from constants import Gender, Role

# class ManageUserForm(forms.ModelForm):  # Changed to ModelForm for better integration
#     class Meta:
#         model = UserModel
#         fields = [
#             'first_name', 'last_name', 'email', 'dob', 'gender', 'phone', 'address',
#             'country', 'location', 'city', 'district', 'state', 'pincode', 'roles'
#         ]
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
#             'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'gender': forms.Select(attrs={'class': 'form-control'}, choices=[(g.value, g.name) for g in Gender]),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
#             'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
#             'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
#             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
#             'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'}),
#             'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
#             'pincode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'}),
#             'roles': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'role'}),
#         }

#     # Make fields optional to match model
#     first_name = forms.CharField(max_length=100, required=True)
#     last_name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     dob = forms.DateField(required=False)
#     gender = forms.ChoiceField(choices=[(g.value, g.name) for g in Gender], required=False)
#     phone = forms.CharField(max_length=15, required=False)
#     address = forms.CharField(required=False)
#     country = forms.CharField(required=False)
#     location = forms.CharField(max_length=255, required=False)
#     city = forms.CharField(max_length=100, required=False)
#     district = forms.CharField(max_length=100, required=False)
#     state = forms.CharField(max_length=100, required=False)
#     pincode = forms.IntegerField(required=False)  # Changed to IntegerField
#     roles = forms.MultipleChoiceField(
#         choices=[(role.value, role.name) for role in Role],
#         required=False
#     )

#     def clean_roles(self):
#         roles = self.cleaned_data.get('roles')
#         if roles:
#             # Convert string values from form to integers for ArrayField
#             return [int(role) for role in roles]
#         return []


from django import forms
from ..models import UserModel
from constants import Gender, Role  # These should be Python Enums

class ManageUserForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    gender = forms.ChoiceField(
        choices=[(g.value, g.name) for g in Gender],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'})
    )
    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','palceholder': 'Enter your country'})
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
    )
    district = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'})
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'})
    )
    pincode = forms.CharField(
        max_length=6,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'})
    )
    roles = forms.MultipleChoiceField(
    choices=[(role.value, role.name) for role in Role],
    required=False,
    widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'role'})
)

