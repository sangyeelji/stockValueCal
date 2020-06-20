from django.db import models

# Create your models here.
class CompanyData(models.Model):
    companyName = models.CharField(max_length=200)
    stockCode = models.CharField(max_length=200)
    companyBuz = models.TextField()
    companyCEO = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyName