from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from ..models import ProductsModel

class ManageProductForm(forms.ModelForm):

    name = forms.CharField(
        min_length=3,
        max_length=50,
        validators=[
            MinLengthValidator(3, message="Product name must be at least 3 characters long."),
            MaxLengthValidator(100, message="Product name cannot exceed 100 characters.")
        ],
        widget=forms.TextInput(attrs={'id': 'product-name', 'class': 'form-control', 'placeholder': 'Enter product name'})
    )

    product_code = forms.CharField(
        min_length=3,
        max_length=20,
        validators=[
            MinLengthValidator(3, message="Product code must be at least 3 characters."),
            MaxLengthValidator(20, message="Product code cannot exceed 20 characters.")
        ],
        widget=forms.TextInput(attrs={'id': 'product-code', 'class': 'form-control', 'placeholder': 'Enter product code'})
    )

    description = forms.CharField(
        required=False,
        min_length=5,
        max_length=500,
        validators=[
            MinLengthValidator(5, message="Description must be at least 5 characters."),
            MaxLengthValidator(500, message="Description cannot exceed 500 characters.")
        ],
        widget=forms.Textarea(attrs={'id': 'product-description', 'class': 'form-control', 'rows': 2, 'placeholder': 'Enter description'})
    )

    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0, message="Price must be a positive number.")],
        widget=forms.NumberInput(attrs={'id': 'product-price', 'class': 'form-control', 'placeholder': 'Enter price'})
    )

    discount_per = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0, message="Discount must be a positive number.")],
        widget=forms.NumberInput(attrs={'id': 'product-discount', 'class': 'form-control', 'placeholder': 'Enter discount percentage'})
    )

    quantity = forms.IntegerField(
        validators=[MinValueValidator(0, message="Quantity must be zero or more.")],
        widget=forms.NumberInput(attrs={'id': 'product-quantity', 'class': 'form-control', 'placeholder': 'Enter quantity'})
    )

    maf_date = forms.DateField(
        widget=forms.DateInput(attrs={'id': 'product-maf', 'class': 'form-control', 'type': 'date'})
    )

    exp_date = forms.DateField(
        widget=forms.DateInput(attrs={'id': 'product-exp', 'class': 'form-control', 'type': 'date'})
    )

    image_urls = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'id': 'product-image', 'class': 'form-control', 'rows': 2, 'placeholder': 'Enter image URLs (comma-separated)'})
    )

    others_category = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'product-others', 'class': 'form-control', 'placeholder': 'Enter other category'})
    )

    class Meta:
        model = ProductsModel
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'id': 'product-category', 'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'id': 'product-subcategory', 'class': 'form-control'}),
        }
