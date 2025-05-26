
from django import forms
from ..models import ProductsModel

class ManageProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Set custom empty labels for dropdowns
        self.fields['category'].empty_label = "Select"
        self.fields['sub_category'].empty_label = "Select"

    class Meta:
        model = ProductsModel
        fields = [
            'name', 'price', 'discount_per', 'quantity', 'maf_date', 'exp_date',
            'product_code', 'description', 'category', 'sub_category', 'others_category'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                'id': 'id_name',
                "placeholder": "Enter product name"
            }),
            'price': forms.NumberInput(attrs={
                "class": "form-control",
                'id': 'id_price',
                "placeholder": "Enter price"
            }),
            'discount_per': forms.NumberInput(attrs={
                "class": "form-control",
                'id': 'id_discount_per',
                "placeholder": "Enter discount percentage"
            }),
            'quantity': forms.NumberInput(attrs={
                "class": "form-control",
                'id': 'id_quantity',
                "placeholder": "Enter quantity"
            }),
            'maf_date': forms.DateInput(attrs={
                "class": "form-control",
                'id': 'id_maf_date',
                "type": "date"
            }),
            'exp_date': forms.DateInput(attrs={
                "class": "form-control",
                'id': 'id_exp_date',
                "type": "date"
            }),
            'product_code': forms.TextInput(attrs={
                "class": "form-control",
                'id': 'id_product_code',
                "placeholder": "Enter product code"
            }),
            'description': forms.Textarea(attrs={
                "class": "form-control",
                'id': 'id_description',
                "placeholder": "Enter description",
                "rows": 2
            }),
            'category': forms.Select(attrs={
                "class": "form-control",
                'id': 'id_category'
            }),
            'sub_category': forms.Select(attrs={
                "class": "form-control",
                'id': 'id_sub_category'
            }),
            'others_category': forms.TextInput(attrs={
                "class": "form-control",
                'id': 'id_others_category',
                "placeholder": "Enter other category"
            }),
        }

        labels = {
            'name': "Product Name",
            'price': "Price",
            'discount_per': "Discount Percentage",
            'quantity': "Quantity",
            'maf_date': "Manufacturing Date",
            'exp_date': "Expiration Date",
            'product_code': "Product Code",
            'description': "Description",
            'category': "Category",
            'sub_category': "Sub Category",
            'others_category': "Other Category",
        }

