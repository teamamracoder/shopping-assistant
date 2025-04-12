
from django import forms
from ..models import ProductsModel
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator


class ManageProductForm(forms.ModelForm):
    """Form for updating a product with inline field validation"""

    # ✅ Don't repeat 'name' widget in Meta if defining it here
    name = forms.CharField(
        min_length=5,
        max_length=50,
        validators=[
            MinLengthValidator(5, message="Product name must be at least 5 characters long."),
            MaxLengthValidator(50, message="Product name cannot exceed 50 characters."),
        ],
        widget=forms.TextInput(attrs={
            'id': 'product-name',
            'class': 'form-control',
            'placeholder': 'Enter product name'
        })
    )

    price = forms.DecimalField(
        min_value=0.01,
        widget=forms.NumberInput(attrs={
            'id': 'product-price',
            'class': 'form-control',
            'placeholder': 'Enter price'
        }),
        error_messages={'min_value': 'Price must be greater than 0.'}
    )

    discount_per = forms.DecimalField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'id': 'product-discount',
            'class': 'form-control',
            'placeholder': 'Enter discount percentage'
        }),
        error_messages={
            'min_value': 'Discount cannot be negative.',
            'max_value': 'Discount cannot exceed 100%.'
        }
    )

    quantity = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'id': 'product-quantity',
            'class': 'form-control',
            'placeholder': 'Enter quantity'
        }),
        error_messages={'min_value': 'Quantity cannot be negative.'}
    )

    maf_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'product-maf',
            'class': 'form-control',
            'type': 'date'
        })
    )

    exp_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'product-exp',
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = ProductsModel
        fields = '__all__'

        widgets = {
            'product_code': forms.TextInput(attrs={
                'id': 'product-code',
                'class': 'form-control',
                'placeholder': 'Enter product code'
            }),
            'description': forms.Textarea(attrs={
                'id': 'product-description',
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter description'
            }),
            # 'image_urls': forms.Textarea(attrs={'id': 'product-image', 'class': 'form-control', 'rows': 2, 'placeholder': 'Enter image URLs (comma-separated)'}),

            'category': forms.Select(attrs={
                'id': 'product-category',
                'class': 'form-control'
            }),
            'sub_category': forms.Select(attrs={
                'id': 'product-subcategory',
                'class': 'form-control'
            }),
            'others_category': forms.TextInput(attrs={
                'id': 'product-others',
                'class': 'form-control',
                'placeholder': 'Enter other category'
            }),
        }
