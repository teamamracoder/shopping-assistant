from django import forms
from ..models import UserModel

class ManageUserCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}))
    contact = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}))
    pincode = forms.CharField(max_length=6, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'}))



class ManageUserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel()
        fields = [
            "first_name", "last_name", "email", "dob", "gender", "phone",
            "address", "location", "city", "district", "state", "pincode"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "gender": forms.Select(attrs={"class": "form-select"}, choices=[("M", "Male"), ("F", "Female")]),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "pincode": forms.NumberInput(attrs={"class": "form-control"}),
        }


# class ManageUserUpdateForm(forms.Form):
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     phone = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'class': 'form-control'}))  # ✅ Changed contact to phone
#     address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     pincode = forms.CharField(max_length=6, widget=forms.NumberInput(attrs={'class': 'form-control'}))




# class ManageUserUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
#     dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}))
#     contact = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}))
#     address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}))
#     location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}))
#     district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your district'}))
#     state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}))
#     pincode = forms.CharField(max_length=6, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'}))
#     labels = {
#             'first_name': "First Name",
#             'middle_name': "Middle Name",
#             'last_name': "Last Name",
#             'dob': "Date of Birth",
#             'address': "Address",
#             'hobbies': "Hobbies",
#         }

#     middle_name = forms.CharField(
#         label="Middle Name",
#         required=False,  # Middle name is optional
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your middle name"})
#     )