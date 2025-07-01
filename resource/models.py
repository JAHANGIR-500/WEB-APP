from django.db import models
class Resource(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the auto-incrementing ID
    RESOURCE_UNITS = [
        ('Pcs', 'Pcs'),
        ('Nos', 'Nos'),
        ('Kg', 'Kg'),
        ('Lit', 'Lit'),
    ]
    RESOURCE_GROUPS = [
        ('Civil', 'Civil work Material'),
        ('Sanitary', 'Sanitary work Material'),
        ('Electrical', 'Electrical work Material'),
        ('NA', 'NA'),
    ]
    name_of_resource = models.CharField(max_length=100, verbose_name='Name of Resource')
    resource_unit = models.CharField(max_length=10, choices=RESOURCE_UNITS, verbose_name='Resource Unit')
    resource_group = models.CharField(max_length=20, choices=RESOURCE_GROUPS, verbose_name='Group of Resource')
    def __str__(self):
        return self.name_of_resource  # Updated for renamed field

