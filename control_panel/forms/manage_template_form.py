from django import forms
from ..models import TemplateModel


class ManageTemplateForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = ['subject', 'body', 'payload', 'link', 'placeholders']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'payload': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'placeholders': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }

