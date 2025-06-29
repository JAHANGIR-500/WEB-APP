from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name_of_employee', 'employee_address', 'employee_email', 'employee_contact']
        labels = {
            'name_of_employee': 'Employee Name',
            'employee_address': 'Address',
            'employee_email': 'Email',
            'employee_contact': 'Contact Number',
        }
        widgets = {
            'name_of_employee': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee name'
            }),
            'employee_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee address'
            }),
            'employee_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee email'
            }),
            'employee_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
        }
