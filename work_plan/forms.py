from django import forms
from .models import WorkPlan
class WorkPlanForm(forms.ModelForm):
    class Meta:
        model = WorkPlan
        fields = [
            'project',
            'category_project',
            'client',
            'task',
            'category_drawing',
            'planned_start',
            'planned_finish',
            'start_date',
            'finish_date',
            'progress',
        ]
        widgets = {
            'planned_start': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'planned_finish': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'finish_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'progress': forms.NumberInput(attrs={'min': 0, 'max': 100, 'class': 'form-control'}),
            
        }
