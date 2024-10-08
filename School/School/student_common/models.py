from django.db import models

# Create your models here.

class Employee(models.Model):
    sno = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=255,default='')
    Employee_id = models.CharField(max_length=255, default='',unique=True)
    Employee_Department = models.CharField(max_length=255,default='')


class Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, default='')
    Email_id = models.CharField(max_length=255,unique=True)
    Password = models.CharField(max_length=255)
    Gender = models.CharField(max_length=50)
    State = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=255,unique=True)