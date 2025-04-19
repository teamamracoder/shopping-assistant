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

    # Corrected Name Field Validation
    # name = forms.CharField(
    #     min_length=3,
    #     max_length=50,
    #     validators=[
    #         MinLengthValidator(3, message="Category name must be at least 3 characters long."),
    #         MaxLengthValidator(50, message="Category name cannot exceed 50 characters."),  # Fixed max length message
    #     ],
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter category name"})
    # )
