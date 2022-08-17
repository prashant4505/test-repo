from django.db import models

# Create your models here.

class Login(models.Model):
    uid=models.IntegerField()
    umail=models.CharField(max_length=50)
    upass=models.CharField(max_length=50) 
    
class ContactUs(models.Model):
    full_name=models.CharField(max_length=50)
    umail=models.CharField(max_length=50)
    qry=models.CharField(max_length=500)

class addStudent(models.Model):
    full_name=models.CharField(max_length=50)
    umail=models.CharField(max_length=50)
    contact_num=models.CharField(max_length=10)
    course=models.CharField(max_length=50)

class addStaff(models.Model):
    full_name=models.CharField(max_length=50)
    umail=models.CharField(max_length=50)
    contact_num=models.CharField(max_length=10)
    department=models.CharField(max_length=50)