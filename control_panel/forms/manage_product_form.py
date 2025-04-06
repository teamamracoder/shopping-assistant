from django import forms
from ..models import ProductsModel, ProductCategoryModel, ProductSubCategoryModel

class ManageProductForm(forms.ModelForm):
    """Form for updating a product"""

    class Meta:
        model = ProductsModel
        fields = '__all__'  # Ensure all fields are included

        widgets = {
            'name': forms.TextInput(attrs={'id': 'product-name', 'class': 'form-control', 'placeholder': 'Enter product name'}),
            'product_code': forms.TextInput(attrs={'id': 'product-code', 'class': 'form-control', 'placeholder': 'Enter product code'}),
            'description': forms.Textarea(attrs={'id': 'product-description', 'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'price': forms.NumberInput(attrs={'id': 'product-price', 'class': 'form-control', 'placeholder': 'Enter price'}),
            'discount_per': forms.NumberInput(attrs={'id': 'product-discount', 'class': 'form-control', 'placeholder': 'Enter discount percentage'}),
            'quantity': forms.NumberInput(attrs={'id': 'product-quantity', 'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'maf_date': forms.DateInput(attrs={'id': 'product-maf', 'class': 'form-control', 'type': 'date'}),
            'exp_date': forms.DateInput(attrs={'id': 'product-exp', 'class': 'form-control', 'type': 'date'}),
            'image_urls': forms.Textarea(attrs={'id': 'product-image', 'class': 'form-control', 'rows': 2, 'placeholder': 'Enter image URLs (comma-separated)'}),
            'category': forms.Select(attrs={'id': 'product-category', 'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'id': 'product-subcategory', 'class': 'form-control'}),
            'others_category': forms.TextInput(attrs={'id': 'product-others', 'class': 'form-control', 'placeholder': 'Enter other category'}),
            # 'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }