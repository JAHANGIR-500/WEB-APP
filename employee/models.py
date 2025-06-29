from django.db import models
class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name_of_employee = models.CharField(max_length=255)  # Full name of the employee
    employee_address = models.CharField(max_length=500)  # Address of the employee
    employee_email = models.EmailField(unique=True)  # Unique email address
    employee_contact = models.CharField(max_length=20)  # Contact phone number
    def __str__(self):
        return f"{self.name_of_employee}"
