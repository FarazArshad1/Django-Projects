from django.db import models

# Create your models here.

class Employee(models.Model):
    sno = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=255,default='')
    Employee_id = models.CharField(max_length=255, default='',unique=True)
    Employee_Department = models.CharField(max_length=255,default='')
