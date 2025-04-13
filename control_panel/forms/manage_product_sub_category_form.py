from django import forms
from ..models import ProductSubCategoryModel
from django.core.validators import MinLengthValidator, MaxLengthValidator


class ManageProductSubCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductSubCategoryModel
        fields = '__all__'  # Ensure all fields are included

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name', 'id': 'id_name', 'placeholder': 'Enter subcategory name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'name': 'description', 'id': 'id_description', 'rows': 2, 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-control', 'name': 'category', 'id': 'id_category'}),
        }