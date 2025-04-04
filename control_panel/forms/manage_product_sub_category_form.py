from django import forms
from ..models import ProductSubCategoryModel
from django.core.validators import MinLengthValidator, MaxLengthValidator


class ManageProductSubCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductSubCategoryModel
        fields = ['category', 'name', 'description']  # Added 'is_active'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name', 'placeholder': 'Enter subcategory name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description', 'rows': 3, 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
        }

    name = forms.CharField(
        min_length=3,
        max_length=50,
        validators=[
            MinLengthValidator(5, message="Product sub category name must be at least 5 characters long."),
            MaxLengthValidator(50, message="Product sub category  cannot exceed 50 characters."),  # Fixed max length message
        ],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subcategory name'}),
    )

    description = forms.CharField(
        required=False,
        min_length=20,
        max_length=300,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
    )