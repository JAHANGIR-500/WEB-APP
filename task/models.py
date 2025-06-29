from django.db import models
class Task(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name_of_task = models.CharField(max_length=255)  # Name of the task
    group_of_task = models.CharField(max_length=255)  # Group the task belongs to
    def __str__(self):
        return f"{self.name_of_task}"

