from django import forms
from ..models import ProductSubCategoryModel
from django.core.validators import MinLengthValidator, MaxLengthValidator


class ManageProductSubCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductSubCategoryModel
        fields = '__all__'  # Ensure all fields are included

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name', 'placeholder': 'Enter subcategory name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description', 'rows': 2, 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

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
