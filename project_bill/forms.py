from django import forms
from django.urls import reverse_lazy
from django_select2.forms import ModelSelect2Widget
from .models import ProjectBill, Project, Contractor

class ProjectBillForm(forms.ModelForm):
    class Meta:
        model = ProjectBill
        fields = [
            'project', 'contractor', 'work_name', 'work_type',
            'location', 'work_unit', 'quantity', 'unit_rate'
        ]
        widgets = {
            'project': ModelSelect2Widget(
                model=Project,
                search_fields=['name__icontains'],
                url=reverse_lazy('project-autocomplete'),
                attrs={'data-placeholder': 'Search project', 'style': 'width:100%;'}
            ),
            'contractor': ModelSelect2Widget(
                model=Contractor,
                search_fields=['company_name__icontains'],
                url=reverse_lazy('contractor-autocomplete'),
                attrs={'data-placeholder': 'Search contractor', 'style': 'width:100%;'}
            ),
            'work_name': forms.TextInput(attrs={'class': 'form-control'}),
            'work_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'work_unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }




