from django import forms
from .models import Resource
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name_of_resource', 'resource_unit', 'resource_group']
        labels = {
            'name_of_resource': 'Name of Resource',
            'resource_unit': 'Resource Unit',
            'resource_group': 'Group of Resource',
        }
        widgets = {
            'name_of_resource': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter resource name'
            }),
            'resource_unit': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter resource unit'
            }),
            'resource_group': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter resource group'
            }),
        }
