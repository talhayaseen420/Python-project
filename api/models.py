from django.db import models

# Create your models here.
#Company modal

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField(default='Your default value here')
    type = models.CharField(max_length=50, choices=(('IT', 'IT'), ('NON IT', 'NON IT')))
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('manager', 'manager'), ('sd' , 'sd') , ('leader', 'leader')))
    
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
