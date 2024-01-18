from django.db import models

# Create your models here.

# creating company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices = (
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('M_Phn','M_Phn')
        ))
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    def __str__(self, ):
        return self.name


# Employee model
        
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phn_no = models.CharField(max_length=10)
    skill = models.CharField(max_length=100, choices = (
        ('frontend developer', 'frontend developer'),
        ('Backend developer', 'Backend developer'),
        ('Database Adminstrator', 'Database Adminstrator'),
        ('Non IT Skills', 'Non IT Skills'),
    ))
    added_date = models.DateTimeField(auto_now = True)
    employeeOf = models.ForeignKey("Company", on_delete=models.CASCADE)
