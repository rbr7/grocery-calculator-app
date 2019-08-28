from django.db import models

# Create your models here.
class NewUser(models.Model):
    username= models.CharField(max_length=15)
    emailid=models.CharField(max_length=30)
    phoneno=models.CharField(max_length=15)
    password=models.CharField(max_length=15)


class LoggedinUser(models.Model):
    username=models.CharField(max_length=15)
    emailid= models.CharField(max_length=15)


class ProductList(models.Model):
    emailid=models.CharField(max_length=30)
    myList=models.TextField(null=True)
    myListOwn=models.TextField(null=True)
