from django import forms
from .models import Contractor
class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['company_name', 'contractor_name', 'contractor_address', 'contact_number']
        labels = {
            'company_name': 'Contractor Company Name',
            'contractor_name': 'Contractor Name',
            'contractor_address': 'Contractor Address',
            'contact_number': 'Contact Number',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'contractor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contractor name'}),
            'contractor_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
        }
