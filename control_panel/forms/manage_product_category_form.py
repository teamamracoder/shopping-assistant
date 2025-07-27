from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from ..models import ProductCategoryModel

class ManageProductCategoryForm(forms.ModelForm):
    
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'  # Ensure all fields are included
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control",'name': 'name','id': 'id_name', "placeholder": "Enter category name"}),
            'description': forms.Textarea(attrs={"class": "form-control",'name': 'descripyion','id': 'id_description', "placeholder": "Enter description", "rows": 1}),
            # 'is_active': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
        labels = {
            'name': "Category Name",
            'description': "Description",
            'is_active': "Active",
        }