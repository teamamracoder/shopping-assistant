from django import forms
from ..models import ProductSubCategoryModel

class ManageProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategoryModel
        fields = ['category', 'name', 'description', 'is_active']  # Added 'is_active'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subcategory name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
