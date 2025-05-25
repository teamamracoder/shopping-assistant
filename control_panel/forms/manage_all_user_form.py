# from django import forms
# from ..models import UserModel
# from django import forms
# from ..models import UserModel
# from constants import Gender,Role

# class ManageUserForm(forms.Form):
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





# class ManageUserForm(forms.ModelForm):
#     class Meta:
#         model = UserModel  # Specify the model to which the form is bound
#         fields = ['first_name', 'last_name', 'email', 'dob', 'gender', 'phone', 'address', 'location', 'city', 'district', 'state', 'pincode','roles']
       

#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'user-first-name', 'class': 'form-control', 'placeholder': 'Enter first name'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'user-last-name', 'class': 'form-control', 'placeholder': 'Enter last name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'user-email', 'class': 'form-control', 'placeholder': 'Enter your email'}))
#     dob = forms.DateField(widget=forms.DateInput(attrs={'id': 'user-dob', 'class': 'form-control', 'type': 'date'}))
#     gender = forms.ChoiceField(
#     choices=[(gender.value, gender.name) for gender in Gender],
#     widget=forms.Select(attrs={'id': 'user-gender', 'class': 'form-control'})
# )
#     phone = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'id': 'user-phone', 'class': 'form-control', 'placeholder': 'Enter your contact number'}))
#     address = forms.CharField(widget=forms.TextInput(attrs={'id': 'user-address', 'class': 'form-control', 'placeholder': 'Enter your address'}))
#     location = forms.CharField(widget=forms.TextInput(attrs={'id': 'user-location', 'class': 'form-control', 'placeholder': 'Enter your location'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'id': 'user-city', 'class': 'form-control', 'placeholder': 'Enter your city'}))
#     district = forms.CharField(widget=forms.TextInput(attrs={'id': 'user-district', 'class': 'form-control', 'placeholder': 'Enter your district'}))
#     state = forms.CharField(widget=forms.TextInput(attrs={'id': 'user-state', 'class': 'form-control', 'placeholder': 'Enter your state'}))
#     pincode = forms.CharField(max_length=6, widget=forms.NumberInput(attrs={'id': 'user-pincode', 'class': 'form-control', 'placeholder': 'Enter your pincode'}))
#     roles = forms.MultipleChoiceField(
#     choices=[(role.value, role.name) for role in Role],
#     required=False,
#     widget=forms.CheckboxSelectMultiple  # or SelectMultiple
# )




    
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

