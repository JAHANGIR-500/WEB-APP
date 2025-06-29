from django.db import models
from decimal import Decimal
from project.models import Project
from customer.models import Customer
class SalesBill(models.Model):
    LOCATION_CHOICES = [
        ('GF', 'GF'), ('1F', '1F'), ('2F', '2F'), ('3F', '3F'),
        ('4F', '4F'), ('5F', '5F'), ('6F', '6F'), ('7F', '7F'), ('RF', 'RF'),
    ]
    FLAT_TYPE_CHOICES = [
        ('Flat-A', 'Flat-A'), ('Flat-B', 'Flat-B'), ('Flat-C', 'Flat-C'),
    ]
    UNIT_CHOICES = [
        ('Sft', 'Sft'),
    ]
    id = models.AutoField(primary_key=True)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    flat_type = models.CharField(max_length=10, choices=FLAT_TYPE_CHOICES)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    
    
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def save(self, *args, **kwargs):
        if self.quantity is not None and self.unit_rate is not None:
            self.bill_amount = Decimal(str(self.quantity)) * self.unit_rate
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Bill #{self.id} — {self.project_name.name_of_project} for {self.customer_name.customer_name}"
