from django import forms
from ..models import ProductCategoryModel

class ManageProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryModel
        fields = ['name', 'description', 'is_active']
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter category name"}),
            'description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description", "rows": 3}),
            'is_active': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
        labels = {
            'name': "Category Name",
            'description': "Description",
            'is_active': "Active",
        }
