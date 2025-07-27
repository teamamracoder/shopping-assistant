from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from ..models import StoreCategoryModel

class ManageStoreCategoryForm(forms.ModelForm):

    class Meta:
        model = StoreCategoryModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'name': 'name','id': 'id_name', "placeholder": "Enter category name"}),
        }

        labels = {
            'name': "Store Category Name",
            'is_active': "Active",
        }
