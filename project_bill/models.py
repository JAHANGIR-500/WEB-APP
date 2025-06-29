from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class ProjectBill(models.Model):
    TYPE_OF_WORK_CHOICES = [('SAM', 'SAM')]
    LOCATION_CHOICES = [(f'{f}', f'{f}') for f in ['GF', '1F', '2F', '3F', '4F', '5F', '6F', '7F', 'RF']]
    WORK_UNIT_CHOICES = [('Sft', 'Sft')]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    work_name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=10, choices=TYPE_OF_WORK_CHOICES)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    work_unit = models.CharField(max_length=10, choices=WORK_UNIT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bill_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.bill_amount = (self.quantity * self.unit_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill for {self.work_name} ({self.project.name})"
