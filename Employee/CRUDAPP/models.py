from django.db import models

# Create your models here.

class Employee(models.Model):
    EmpId = models.CharField(max_length=30)
    EmpName = models.CharField(max_length=20)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField()
    EmpDesignation = models.CharField(max_length=25)
    class Meta:
        db_table="Employee"
