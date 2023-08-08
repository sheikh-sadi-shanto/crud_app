from django.db import models
from django.utils import timezone


class Person(models.Model):
    
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age = models.IntegerField()
    gender =models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    pic=models.ImageField(upload_to='img')

class Apk(models.Model):
    name=models.CharField(max_length=20)
    file=models.FileField(upload_to='file',blank=True)
    pic=models.ImageField(upload_to='pic')








# Create your models here.
class DETAILS(models.Model):
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='img')
    created=models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return self.name

    
class Time(models.Model):
    last_time=models.DateField(default=timezone.now)
    usert=models.OneToOneField(DETAILS,on_delete=models.CASCADE)