from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_of_task', 'group_of_task']
        labels = {
            'name_of_task': 'Task Name',
            'group_of_task': 'Task Group',
        }
        widgets = {
            'name_of_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task name'
            }),
            'group_of_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task group'
            }),
        }
