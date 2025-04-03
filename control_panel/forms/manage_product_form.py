from django import forms
from ..models import ProductsModel, ProductCategoryModel, ProductSubCategoryModel

class ManageProductForm(forms.ModelForm):
    """Form for updating a product"""

    class Meta:
        model = ProductsModel
        fields = [
            'name', 'product_code', 'description', 'price', 'discount_per', 'quantity', 
            'maf_date', 'exp_date', 'image_urls', 'category', 'sub_category', 'others_category', 'is_active'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'discount_per': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount percentage'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'maf_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'exp_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image_urls': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter image URLs (comma-separated)'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'class': 'form-control'}),
            'others_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter other category'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
