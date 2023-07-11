
from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)



class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Advocate(models.Model):
    name = models.CharField(max_length=200 ,null=True)
    profile = models.TextField(null=True, blank=True,max_length=500)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=200)
    bio =  models.TextField(max_length=200, null=True, blank=True)
    twitter = models.URLField(("Twitter"), max_length=200 ,null=True)

    def __str__(self):
        return self.username
    

