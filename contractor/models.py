from django.db import models
class Contractor(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    contractor_name = models.CharField(max_length=255)
    contractor_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.company_name  # ✅ Only show contractor company name


