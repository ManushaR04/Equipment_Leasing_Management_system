from django.db import models

# Create your models here.
class register(models.Model):

    Name=models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Status = models.BooleanField(default=False)

class uploaddata(models.Model):
    Name = models.CharField(max_length=20)
    Idno = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    Picture = models.FileField()
    Status = models.BooleanField(default=False)
