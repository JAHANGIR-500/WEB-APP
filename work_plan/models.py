from django.db import models
from project.models import Project
from customer.models import Customer
from task.models import Task
from employee.models import Employee

CATEGORY_PROJECT_CHOICES = [
    ('DEA', 'DEA'),
    ('New Design', 'New Design')
]

CATEGORY_DRAWING_CHOICES = [
    ('Main', 'Main'),
    ('Revised-1', 'Revised-1'),
    ('Revised-2', 'Revised-2'),
    ('Revised-3', 'Revised-3'),
    ('Revised-4', 'Revised-4')
]

class WorkPlan(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit ID field

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category_project = models.CharField(max_length=50, choices=CATEGORY_PROJECT_CHOICES)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    category_drawing = models.CharField(max_length=50, choices=CATEGORY_DRAWING_CHOICES)
    planned_start = models.DateField()
    planned_finish = models.DateField()
    start_date = models.DateField()
    finish_date = models.DateField()
    progress = models.PositiveIntegerField(default=0, verbose_name="Progress")
    
    @property
    def planned_duration(self):
        return (self.planned_finish - self.planned_start).days

    @property
    def actual_duration(self):
        return (self.finish_date - self.start_date).days

    @property
    def duration_variance(self):
        return self.actual_duration - self.planned_duration

    def __str__(self):
        return f"{self.project.name_of_project} | {self.task.name_of_task}"

