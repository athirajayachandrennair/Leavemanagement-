
from django.db import models

# Create your models here.
class crud(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200, null=True)
    # image =models.ImageField(null=True,blank=True,upload_to ="images/")

class add(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    phonenumber = models.IntegerField()
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

class users(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
 