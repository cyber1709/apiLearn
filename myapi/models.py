from django.db import models

# Create your models here.
class IOC(models.Model):
    ip = models.CharField(max_length=50, null=True)
    domain = models.CharField(max_length=100, null=True)
    noticed_date = models.DateTimeField(max_length=50, null=True)
    source = models.CharField(max_length=50, null=True)
    