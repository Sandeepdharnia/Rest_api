from tkinter import CASCADE
from turtle import position
from django.db import models

# Create your models here.

#Company model 

class Company(models.Model):
    company_id =models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), 
                                                     ('Non IT', 'Non IT'), 
                                                     ('Mobiles Phone', 'Mobile Phone')
                                                     ))
    added_date = models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=True)    

    def __str__(self):
        return self.company_name + ' ' + self.location


# Employe model
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
                                                    ('Manager', 'manager'),
                                                    ('Software Devloper', 'sd'),
                                                    ('Project Leader', 'pl')
                                                         ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
