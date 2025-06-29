from django import forms
from .models import SalesBill

class SalesBillForm(forms.ModelForm):
    class Meta:
        model = SalesBill
        fields = ['project_name', 'customer_name', 'location', 'flat_type', 'unit', 'quantity', 'unit_rate']
        labels = {
            'project_name': 'Project Name',
            'customer_name': 'Customer Name',
            'location': 'Location',
            'flat_type': 'Flat Type',
            'unit': 'Unit',
            'quantity': 'Quantity',
            'unit_rate': 'Unit Rate',
        }
        widgets = {
            'project_name': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'flat_type': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
