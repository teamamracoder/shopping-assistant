from django import forms
from ..models import TemplateModel


class ManageTemplateForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = ['subject', 'body', 'payload', 'link', 'placeholders']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'subject', 'name': 'subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'id': 'body', 'name': 'body'}),
            'payload': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'id': 'payload', 'name': 'payload'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'link', 'name': 'link'}),
            'placeholders': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'id': 'placeholders', 'name': 'placeholders'}),
        }

