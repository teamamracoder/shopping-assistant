from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from ..models import ProductCategoryModel

class ManageProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryModel
        fields = ['name', 'description', 'is_active']
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter category name"}),
            'description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description", "rows": 3}),
            # 'is_active': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
        labels = {
            'name': "Category Name",
            'description': "Description",
            'is_active': "Active",
        }

    # Corrected Name Field Validation
    name = forms.CharField(
        min_length=3,
        max_length=50,
        validators=[
            MinLengthValidator(3, message="Category name must be at least 3 characters long."),
            MaxLengthValidator(50, message="Category name cannot exceed 50 characters."),  # Fixed max length message
        ],
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter category name"})
    )

    # Corrected Description Field Validation
    description = forms.CharField(
        min_length=20,
        max_length=300,  # Matching the MaxLengthValidator
        required=False,  # Optional field
        validators=[
            MinLengthValidator(20, message="Description must be at least 20 characters long."),
            MaxLengthValidator(300, message="Description cannot exceed 300 characters.")  # Fixed max length
        ],
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description", "rows": 3})
    )
