from django.db import models

# Create your models here.

class Employee(models.Model):
    sno = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=255,default='')
    Employee_id = models.CharField(max_length=255, default='',unique=True)
    Employee_Department = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.Employee_name


class Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, default='')
    Email_id = models.CharField(max_length=255,unique=True)
    Password = models.CharField(max_length=255)
    Gender = models.CharField(max_length=50)
    State = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.Email_id


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255)
    """ To change the name to person_name". Had to run the makemigration and migrate command twice"""
    person_name = models.CharField(max_length=255,db_column='name')
    Email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, default= 'NaN')


class Teacher(models.Model):
    sno = models.AutoField(primary_key=True)
    Teacher_Name = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Salary = models.IntegerField()