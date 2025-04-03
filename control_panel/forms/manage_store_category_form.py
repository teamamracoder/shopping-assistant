from django import forms
from ..models import StoreCategoryModel

class StoreCategoryForm(forms.ModelForm):
    class Meta:
        model = StoreCategoryModel
        fields = ['name', 'is_active', 'created_by', 'updated_by']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-select'}),
            'updated_by': forms.Select(attrs={'class': 'form-select'}),
        }
