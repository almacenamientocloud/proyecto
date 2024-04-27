from django.db import models

class Employee(models.Model): 

    identification = models.CharField(max_length=12) 
    name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=254) 
    salary = models.IntegerField() 
    is_active = models.BooleanField(default=True) 
